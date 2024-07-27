# FITS Viewer Extension

This Visual Studio Code extension allows you to open FITS files in a browser using the Firefly library.

## Features

- Open FITS files directly from the VSCode Explorer.
- View FITS files in a web browser with Firefly.

## Usage

1. Right-click on a FITS file in the VSCode Explorer.
2. Select "Open FITS File" from the context menu.
3. The FITS file will open in your default web browser.

## Development

This uses scafolding code 'yo', installed with:

```bash
npm install -g yo generator-code
```

And run to create the structure of the repos:
```bash
yo code
```

Updates are in `src/extension.ts` and `package.json`

## Installation

### From VSIX File

1. Download the `.vsix` file from the provided link.
2. Open VSCode.
3. Go to the Extensions view (`Ctrl+Shift+X` or `Cmd+Shift+X` on macOS).
4. Click the three-dot menu (`...`) at the top-right corner.
5. Select "Install from VSIX..." and choose the downloaded `.vsix` file.

## Extension Settings

This extension does not require any specific settings.

## Known Issues

- Ensure the FITS file is accessible and not corrupted.

## Release Notes

### 0.0.1

- Initial release of FITS Viewer Extension.

