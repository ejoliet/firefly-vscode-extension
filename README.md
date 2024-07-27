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

This uses scaffolding code 'yo', installed with:

```bash
npm install -g yo generator-code
```

And run to create the structure of the repos:
```bash
yo code
```

Updates are in `src/extension.ts` and `package.json`

### Prerequisites

- [Node.js](https://nodejs.org/) (version 14 or higher recommended)
- [npm](https://www.npmjs.com/) (usually comes with Node.js)
- [Visual Studio Code](https://code.visualstudio.com/)

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/<USERNAME>/fits-viewer-extension.git
    cd fits-viewer-extension
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Build the extension:
    ```bash
    npm run compile
    ```

4. Open the extension in VSCode:
    ```bash
    code .
    ```

5. Launch the extension:
    - Press `F5` to open a new VSCode window with your extension loaded.

## Installation

Build package with

```bash
vsce package
```

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

