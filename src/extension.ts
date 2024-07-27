import * as vscode from 'vscode';
import * as path from 'path';
import * as fs from 'fs';
import * as os from 'os';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.openFitsFile', (uri: vscode.Uri) => {
        const filePath = uri.fsPath;
        if (path.extname(filePath).toLowerCase() === '.fits') {
            generateHtmlAndOpen(filePath);
        } else {
            vscode.window.showErrorMessage('Please select a FITS file.');
        }
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}

function generateHtmlAndOpen(fitsFilePath: string) {
    const tempDir = os.tmpdir();
    const fileName = path.basename(fitsFilePath);
    const fitsFileDest = path.join(tempDir, fileName);
    const htmlFilePath = path.join(tempDir, 'fits-viewer.html');

    // Copy the FITS file to the temporary directory
    fs.copyFileSync(fitsFilePath, fitsFileDest);

    const htmlContent = `
    <!doctype html>
    <html>
    <head>
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Expires" content="0">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>Roman QL</title>
    </head>
    <body>
        <h1> Roman image diagnostic tool template </h1>
        <h3>This file needs to live in firefly server to be working.</h3>
        <div id="plotHere" style="width: 600px; height: 800px;"></div>
        <script type="text/javascript">
            window.firefly = { options: { MenuItemKeys: { showImageToolbar: false } } };
            function onFireflyLoaded() {
                const fitsUrl = 'file:///${fitsFileDest.replace(/\\/g, '/')}'; // Local URL for the FITS file
                firefly.showImage('plotHere', {
                    url: fitsUrl,
                    Title: 'Example FITS Image',
                    ColorTable: 16,
                    RangeValues: firefly.util.image.RangeValues.serializeSimple('Sigma', -2, 8, 'Linear')
                });
            }
        </script>
        <script type="text/javascript" src="https://irsa.ipac.caltech.edu/irsaviewer/firefly_loader.js"></script>
    </body>
    </html>
    `;

    // Write the HTML content to a file
    fs.writeFileSync(htmlFilePath, htmlContent, 'utf8');

    // Open the HTML file in the default browser
    vscode.env.openExternal(vscode.Uri.file(htmlFilePath));
}
