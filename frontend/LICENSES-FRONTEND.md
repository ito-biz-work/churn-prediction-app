### 主要ライブラリおよびライセンス (Third-Party Licenses)

本プロジェクトのフロントエンド（UI/Webアプリケーション構築等）で使用している主要なライブラリおよびそのライセンス一覧です。

┌──────────────────────────────────────────────┬───────────────┬────────────────────────────────────────────────────────────────────────────────────┐
│ Package                                      │ License       │ Details                                                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ tslib                                        │ 0BSD          │ Microsoft Corp.                                                                    │
│                                              │               │ Runtime library for TypeScript helper functions                                    │
│                                              │               │ https://www.typescriptlang.org/                                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint/config-array (dev)                   │ Apache-2.0    │ Nicholas C. Zakas                                                                  │
│                                              │               │ General purpose glob-based configuration matching.                                 │
│                                              │               │ https://github.com/eslint/rewrite/tree/main/packages/config-array#readme           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint/config-helpers (dev)                 │ Apache-2.0    │ Helper utilities for creating ESLint configuration                                 │
│                                              │               │ https://github.com/eslint/rewrite/tree/main/packages/config-helpers#readme         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint/core (dev)                           │ Apache-2.0    │ Nicholas C. Zakas                                                                  │
│                                              │               │ Runtime-agnostic core of ESLint                                                    │
│                                              │               │ https://github.com/eslint/rewrite/tree/main/packages/core#readme                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint/object-schema (dev)                  │ Apache-2.0    │ Nicholas C. Zakas                                                                  │
│                                              │               │ An object schema merger/validator                                                  │
│                                              │               │ https://github.com/eslint/rewrite/tree/main/packages/object-schema#readme          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint/plugin-kit (dev)                     │ Apache-2.0    │ Nicholas C. Zakas                                                                  │
│                                              │               │ Utilities for building ESLint plugins.                                             │
│                                              │               │ https://github.com/eslint/rewrite/tree/main/packages/plugin-kit#readme             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @humanfs/core (dev)                          │ Apache-2.0    │ Nicholas C. Zakas                                                                  │
│                                              │               │ The core of the humanfs library.                                                   │
│                                              │               │ https://github.com/humanwhocodes/humanfs#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @humanfs/node (dev)                          │ Apache-2.0    │ Nicholas C. Zakas                                                                  │
│                                              │               │ The Node.js bindings of the humanfs library.                                       │
│                                              │               │ https://github.com/humanwhocodes/humanfs#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @humanfs/types (dev)                         │ Apache-2.0    │ Nicholas C. Zakas                                                                  │
│                                              │               │ The TypeScript types for the hfs project.                                          │
│                                              │               │ https://github.com/humanwhocodes/humanfs#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @humanwhocodes/module-importer (dev)         │ Apache-2.0    │ Nicholas C. Zaks                                                                   │
│                                              │               │ Universal module importer for Node.js                                              │
│                                              │               │ https://github.com/humanwhocodes/module-importer#readme                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @humanwhocodes/retry (dev)                   │ Apache-2.0    │ Nicholas C. Zaks                                                                   │
│                                              │               │ A utility to retry failed async methods.                                           │
│                                              │               │ https://github.com/humanwhocodes/retry#readme                                      │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @internationalized/date                      │ Apache-2.0    │ Internationalized calendar, date, and time manipulation utilities                  │
│                                              │               │ https://github.com/adobe/react-spectrum/tree/main#readme                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @internationalized/number                    │ Apache-2.0    │ Internationalized number formatting and parsing utilities                          │
│                                              │               │ https://github.com/adobe/react-spectrum#readme                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @swc/helpers                                 │ Apache-2.0    │ 강동윤                                                                             │
│                                              │               │ Ex                                                                                 │
│                                              │               │ ernal helpers for the swc project.                                                 │
│                                              │               │ ht                                                                                 │
│                                              │               │ ps://swc.rs                                                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ baseline-browser-mapping (dev)               │ Apache-2.0    │ A library for obtaining browser versions with their maximum supported Baseline     │
│                                              │               │ feature set and Widely Available status.                                           │
│                                              │               │ https://github.com/web-platform-dx/baseline-browser-mapping#readme                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ detect-libc (dev)                            │ Apache-2.0    │ Lovell Fuller                                                                      │
│                                              │               │ Node.js module to detect the C standard library (libc) implementation family and   │
│                                              │               │ version                                                                            │
│                                              │               │ https://github.com/lovell/detect-libc#readme                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ eslint-visitor-keys (dev)                    │ Apache-2.0    │ Toru Nagashima                                                                     │
│                                              │               │ Constants and utilities about visitor keys to traverse AST.                        │
│                                              │               │ https://github.com/eslint/js/blob/main/packages/eslint-visitor-keys/README.md      │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ typescript (dev)                             │ Apache-2.0    │ Microsoft Corp.                                                                    │
│                                              │               │ TypeScript is a language for application scale JavaScript development              │
│                                              │               │ https://www.typescriptlang.org/                                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ jackspeak (dev)                              │ BlueOak-1.0.0 │ Isaac Z. Schlueter                                                                 │
│                                              │               │ A very strict and proper argument parser.                                          │
│                                              │               │ https://github.com/isaacs/jackspeak#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ minimatch (dev)                              │ BlueOak-1.0.0 │ Isaac Z. Schlueter                                                                 │
│                                              │               │ a glob matcher in javascript                                                       │
│                                              │               │ https://github.com/isaacs/minimatch#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ minipass (dev)                               │ BlueOak-1.0.0 │ Isaac Z. Schlueter                                                                 │
│                                              │               │ minimal implementation of a PassThrough stream                                     │
│                                              │               │ https://github.com/isaacs/minipass#readme                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ package-json-from-dist (dev)                 │ BlueOak-1.0.0 │ Isaac Z. Schlueter                                                                 │
│                                              │               │ Load the local package.json from either src or dist folder                         │
│                                              │               │ https://github.com/isaacs/package-json-from-dist#readme                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ path-scurry (dev)                            │ BlueOak-1.0.0 │ Isaac Z. Schlueter                                                                 │
│                                              │               │ walk paths fast and efficiently                                                    │
│                                              │               │ https://github.com/isaacs/path-scurry#readme                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ eslint-scope (dev)                           │ BSD-2-Clause  │ ECMAScript scope analyzer for ESLint                                               │
│                                              │               │ https://github.com/eslint/js/blob/main/packages/eslint-scope/README.md             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ espree (dev)                                 │ BSD-2-Clause  │ Nicholas C. Zakas                                                                  │
│                                              │               │ An Esprima-compatible JavaScript parser built on Acorn                             │
│                                              │               │ https://github.com/eslint/js/blob/main/packages/espree/README.md                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ esrecurse (dev)                              │ BSD-2-Clause  │ ECMAScript AST recursive visitor                                                   │
│                                              │               │ https://github.com/estools/esrecurse                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ estraverse (dev)                             │ BSD-2-Clause  │ ECMAScript JS AST traversal functions                                              │
│                                              │               │ https://github.com/estools/estraverse                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ esutils (dev)                                │ BSD-2-Clause  │ utility box for ECMAScript language tools                                          │
│                                              │               │ https://github.com/estools/esutils                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ uri-js (dev)                                 │ BSD-2-Clause  │ Gary Court                                                                         │
│                                              │               │ An RFC 3986/3987 compliant, scheme extendable URI/IRI parsing/validating/resolving │
│                                              │               │ library for JavaScript.                                                            │
│                                              │               │ https://github.com/garycourt/uri-js                                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ esquery (dev)                                │ BSD-3-Clause  │ Joel Feenstra                                                                      │
│                                              │               │ A query library for ECMAScript AST using a CSS selector like query language.       │
│                                              │               │ https://github.com/estools/esquery/                                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ hoist-non-react-statics                      │ BSD-3-Clause  │ Michael Ridgway                                                                    │
│                                              │               │ Copies non-react specific statics from a child component to a parent component     │
│                                              │               │ https://github.com/mridgway/hoist-non-react-statics#readme                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ source-map                                   │ BSD-3-Clause  │ Nick Fitzgerald                                                                    │
│                                              │               │ Generates and consumes source maps                                                 │
│                                              │               │ https://github.com/mozilla/source-map                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ source-map-js (dev)                          │ BSD-3-Clause  │ Valentin 7rulnik Semirulnik                                                        │
│                                              │               │ Generates and consumes source maps                                                 │
│                                              │               │ https://github.com/7rulnik/source-map-js                                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ caniuse-lite (dev)                           │ CC-BY-4.0     │ Ben Briggs                                                                         │
│                                              │               │ A smaller version of caniuse-db, with only the essentials!                         │
│                                              │               │ https://github.com/browserslist/caniuse-lite#readme                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @isaacs/cliui (dev)                          │ ISC           │ Ben Coe                                                                            │
│                                              │               │ easily create complex multi-column command-line-interfaces                         │
│                                              │               │ https://github.com/yargs/cliui#readme                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ electron-to-chromium (dev)                   │ ISC           │ Kilian Valkhof                                                                     │
│                                              │               │ Provides a list of electron-to-chromium version mappings                           │
│                                              │               │ https://github.com/Kilian/electron-to-chromium#readme                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ flatted (dev)                                │ ISC           │ Andrea Giammarchi                                                                  │
│                                              │               │ A super light and fast circular JSON parser.                                       │
│                                              │               │ https://github.com/WebReflection/flatted#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ foreground-child (dev)                       │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ Run a child as if it's the foreground process. Give it stdio. Exit when it exits.  │
│                                              │               │ https://github.com/tapjs/foreground-child#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ glob (dev)                                   │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ the most correct and second fastest glob implementation in JavaScript              │
│                                              │               │ https://github.com/isaacs/node-glob#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ glob-parent (dev)                            │ ISC           │ Gulp Team                                                                          │
│                                              │               │ Extract the non-magic parent path from a glob string.                              │
│                                              │               │ https://github.com/gulpjs/glob-parent#readme                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ graceful-fs (dev)                            │ ISC           │ A drop-in replacement for fs, making various improvements.                         │
│                                              │               │ https://github.com/isaacs/node-graceful-fs#readme                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ isexe (dev)                                  │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ Minimal module to check if a file is executable.                                   │
│                                              │               │ https://github.com/isaacs/isexe#readme                                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ lru-cache (dev)                              │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ A cache object that deletes the least-recently-used items.                         │
│                                              │               │ https://github.com/isaacs/node-lru-cache#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ minimatch (dev)                              │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ a glob matcher in javascript                                                       │
│                                              │               │ https://github.com/isaacs/minimatch#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ picocolors                                   │ ISC           │ Alexey Raspopov                                                                    │
│                                              │               │ The tiniest and the fastest library for terminal output formatting with ANSI       │
│                                              │               │ colors                                                                             │
│                                              │               │ https://github.com/alexeyraspopov/picocolors#readme                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ rimraf (dev)                                 │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ A deep deletion module for node (like `rm -rf`)                                    │
│                                              │               │ https://github.com/isaacs/rimraf#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ semver (dev)                                 │ ISC           │ GitHub Inc.                                                                        │
│                                              │               │ The semantic version parser used by npm.                                           │
│                                              │               │ https://github.com/npm/node-semver#readme                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ signal-exit (dev)                            │ ISC           │ Ben Coe                                                                            │
│                                              │               │ when you want to fire an event no matter how a process exits.                      │
│                                              │               │ https://github.com/tapjs/signal-exit#readme                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ which (dev)                                  │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ Like which(1) unix command. Find the first instance of an executable in the PATH.  │
│                                              │               │ https://github.com/isaacs/node-which#readme                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ yallist (dev)                                │ ISC           │ Isaac Z. Schlueter                                                                 │
│                                              │               │ Yet Another Linked List                                                            │
│                                              │               │ https://github.com/isaacs/yallist#readme                                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ yaml                                         │ ISC           │ Eemeli Aro                                                                         │
│                                              │               │ JavaScript parser and stringifier for YAML                                         │
│                                              │               │ https://eemeli.org/yaml/v1/                                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @alloc/quick-lru (dev)                       │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Simple “Least Recently Used” (LRU) cache                                           │
│                                              │               │ https://github.com/sindresorhus/quick-lru#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @ark-ui/react                                │ MIT           │ A collection of unstyled, accessible UI components for React, utilizing state      │
│                                              │               │ machines for seamless interaction.                                                 │
│                                              │               │ https://ark-ui.com                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/code-frame                            │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Generate errors that contain a code frame that point to source locations.          │
│                                              │               │ https://babel.dev/docs/en/next/babel-code-frame                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/compat-data (dev)                     │ MIT           │ The Babel Team                                                                     │
│                                              │               │ The compat-data to determine required Babel plugins                                │
│                                              │               │ https://github.com/babel/babel#readme                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/core (dev)                            │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Babel compiler core.                                                               │
│                                              │               │ https://babel.dev/docs/en/next/babel-core                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/generator                             │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Turns an AST into code.                                                            │
│                                              │               │ https://babel.dev/docs/en/next/babel-generator                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helper-compilation-targets (dev)      │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Helper functions on Babel compilation targets                                      │
│                                              │               │ https://github.com/babel/babel#readme                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helper-globals                        │ MIT           │ The Babel Team                                                                     │
│                                              │               │ A collection of JavaScript globals for Babel internal usage                        │
│                                              │               │ https://github.com/babel/babel#readme                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helper-module-imports                 │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Babel helper functions for inserting module loads                                  │
│                                              │               │ https://babel.dev/docs/en/next/babel-helper-module-imports                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helper-module-transforms (dev)        │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Babel helper functions for implementing ES6 module transformations                 │
│                                              │               │ https://babel.dev/docs/en/next/babel-helper-module-transforms                      │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helper-string-parser                  │ MIT           │ The Babel Team                                                                     │
│                                              │               │ A utility package to parse strings                                                 │
│                                              │               │ https://babel.dev/docs/en/next/babel-helper-string-parser                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helper-validator-identifier           │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Validate identifier/keywords name                                                  │
│                                              │               │ https://github.com/babel/babel#readme                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helper-validator-option (dev)         │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Validate plugin/preset options                                                     │
│                                              │               │ https://github.com/babel/babel#readme                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/helpers (dev)                         │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Collection of helper functions used by Babel transforms.                           │
│                                              │               │ https://babel.dev/docs/en/next/babel-helpers                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/parser                                │ MIT           │ The Babel Team                                                                     │
│                                              │               │ A JavaScript parser                                                                │
│                                              │               │ https://babel.dev/docs/en/next/babel-parser                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/runtime                               │ MIT           │ The Babel Team                                                                     │
│                                              │               │ babel's modular runtime helpers                                                    │
│                                              │               │ https://babel.dev/docs/en/next/babel-runtime                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/template                              │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Generate an AST from a string template.                                            │
│                                              │               │ https://babel.dev/docs/en/next/babel-template                                      │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/traverse                              │ MIT           │ The Babel Team                                                                     │
│                                              │               │ The Babel Traverse module maintains the overall tree state, and is responsible for │
│                                              │               │ replacing, removing, and adding nodes                                              │
│                                              │               │ https://babel.dev/docs/en/next/babel-traverse                                      │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @babel/types                                 │ MIT           │ The Babel Team                                                                     │
│                                              │               │ Babel Types is a Lodash-esque utility library for AST nodes                        │
│                                              │               │ https://babel.dev/docs/en/next/babel-types                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @chakra-ui/react                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Responsive and accessible React UI components built with React and Emotion         │
│                                              │               │ https://chakra-ui.com/                                                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/babel-plugin                        │ MIT           │ Kye Hohenberger                                                                    │
│                                              │               │ A recommended babel preprocessing plugin for emotion, The Next Generation of       │
│                                              │               │ CSS-in-JS.                                                                         │
│                                              │               │ https://emotion.sh                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/cache                               │ MIT           │ emotion's cache                                                                    │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/hash                                │ MIT           │ A MurmurHash2 implementation                                                       │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/is-prop-valid                       │ MIT           │ A function to check whether a prop is valid for HTML and SVG elements              │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/memoize                             │ MIT           │ emotion's memoize utility                                                          │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/react                               │ MIT           │ Emotion Contributors                                                               │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/serialize                           │ MIT           │ serialization utils for emotion                                                    │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/sheet                               │ MIT           │ emotion's stylesheet                                                               │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/unitless                            │ MIT           │ An object of css properties that don't accept values with units                    │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/use-insertion-effect-with-fallbacks │ MIT           │ A wrapper package that uses `useInsertionEffect` or a fallback for it              │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/utils                               │ MIT           │ internal utils for emotion                                                         │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @emotion/weak-memoize                        │ MIT           │ A memoization function that uses a WeakMap                                         │
│                                              │               │ https://github.com/emotion-js/emotion/tree/main#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint-community/eslint-utils (dev)         │ MIT           │ Toru Nagashima                                                                     │
│                                              │               │ Utilities for ESLint plugins.                                                      │
│                                              │               │ https://github.com/eslint-community/eslint-utils#readme                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint-community/regexpp (dev)              │ MIT           │ Toru Nagashima                                                                     │
│                                              │               │ Regular expression parser for ECMAScript.                                          │
│                                              │               │ https://github.com/eslint-community/regexpp#readme                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @eslint/js (dev)                             │ MIT           │ ESLint JavaScript language implementation                                          │
│                                              │               │ https://eslint.org                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @floating-ui/core                            │ MIT           │ atomiks                                                                            │
│                                              │               │ Positioning library for floating elements: tooltips, popovers, dropdowns, and more │
│                                              │               │ https://floating-ui.com                                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @floating-ui/dom                             │ MIT           │ atomiks                                                                            │
│                                              │               │ Floating UI for the web                                                            │
│                                              │               │ https://floating-ui.com                                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @floating-ui/utils                           │ MIT           │ atomiks                                                                            │
│                                              │               │ Utilities for Floating UI                                                          │
│                                              │               │ https://floating-ui.com                                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @jridgewell/gen-mapping                      │ MIT           │ Justin Ridgewell                                                                   │
│                                              │               │ Generate source maps                                                               │
│                                              │               │ https://github.com/jridgewell/sourcemaps/tree/main/packages/gen-mapping            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @jridgewell/remapping (dev)                  │ MIT           │ Justin Ridgewell                                                                   │
│                                              │               │ Remap sequential sourcemaps through transformations to point at the original       │
│                                              │               │ source code                                                                        │
│                                              │               │ https://github.com/jridgewell/sourcemaps/tree/main/packages/remapping              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @jridgewell/resolve-uri                      │ MIT           │ Justin Ridgewell                                                                   │
│                                              │               │ Resolve a URI relative to an optional base URI                                     │
│                                              │               │ https://github.com/jridgewell/resolve-uri#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @jridgewell/set-array (dev)                  │ MIT           │ Justin Ridgewell                                                                   │
│                                              │               │ Like a Set, but provides the index of the `key` in the backing array               │
│                                              │               │ https://github.com/jridgewell/set-array#readme                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @jridgewell/sourcemap-codec (dev)            │ MIT           │ Justin Ridgewell                                                                   │
│                                              │               │ Encode/decode sourcemap mappings                                                   │
│                                              │               │ https://github.com/jridgewell/sourcemaps/tree/main/packages/sourcemap-codec        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @jridgewell/trace-mapping                    │ MIT           │ Justin Ridgewell                                                                   │
│                                              │               │ Trace the original position through a source map                                   │
│                                              │               │ https://github.com/jridgewell/sourcemaps/tree/main/packages/trace-mapping          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @oxc-project/types (dev)                     │ MIT           │ Boshen and oxc contributors                                                        │
│                                              │               │ Types for Oxc AST nodes                                                            │
│                                              │               │ https://oxc.rs                                                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @pandacss/is-valid-prop                      │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Common error messages for css panda                                                │
│                                              │               │ https://panda-css.com                                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @pkgjs/parseargs (dev)                       │ MIT           │ Polyfill of future proposal for `util.parseArgs()`                                 │
│                                              │               │ https://github.com/pkgjs/parseargs#readme                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @rolldown/binding-linux-x64-gnu (dev)        │ MIT           │ Fast JavaScript/TypeScript bundler in Rust with Rollup-compatible API.             │
│                                              │               │ https://rolldown.rs/                                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @rolldown/pluginutils (dev)                  │ MIT           │ Plugin utilities for Rolldown                                                      │
│                                              │               │ https://github.com/rolldown/plugins/tree/main/packages/pluginutils#readme          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @tailwindcss/node (dev)                      │ MIT           │ A utility-first CSS framework for rapidly building custom user interfaces.         │
│                                              │               │ https://tailwindcss.com                                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @tailwindcss/oxide (dev)                     │ MIT           │ https://github.com/tailwindlabs/tailwindcss#readme                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @tailwindcss/oxide-linux-x64-gnu (dev)       │ MIT           │ https://github.com/tailwindlabs/tailwindcss#readme                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @tailwindcss/postcss (dev)                   │ MIT           │ PostCSS plugin for Tailwind CSS, a utility-first CSS framework for rapidly         │
│                                              │               │ building custom user interfaces                                                    │
│                                              │               │ https://tailwindcss.com                                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @types/esrecurse (dev)                       │ MIT           │ TypeScript definitions for esrecurse                                               │
│                                              │               │ https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/esrecurse     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @types/estree (dev)                          │ MIT           │ TypeScript definitions for estree                                                  │
│                                              │               │ https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/estree        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @types/json-schema (dev)                     │ MIT           │ TypeScript definitions for json-schema                                             │
│                                              │               │ https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/json-schema   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @types/node (dev)                            │ MIT           │ TypeScript definitions for node                                                    │
│                                              │               │ https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/node          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @types/parse-json                            │ MIT           │ TypeScript definitions for parse-json                                              │
│                                              │               │ https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/parse-json    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @types/react                                 │ MIT           │ TypeScript definitions for react                                                   │
│                                              │               │ https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @types/react-dom (dev)                       │ MIT           │ TypeScript definitions for react-dom                                               │
│                                              │               │ https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react-dom     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/eslint-plugin (dev)       │ MIT           │ TypeScript plugin for ESLint                                                       │
│                                              │               │ https://typescript-eslint.io/packages/eslint-plugin                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/parser (dev)              │ MIT           │ An ESLint custom parser which leverages TypeScript ESTree                          │
│                                              │               │ https://typescript-eslint.io/packages/parser                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/project-service (dev)     │ MIT           │ Standalone TypeScript project service wrapper for linting.                         │
│                                              │               │ https://typescript-eslint.io                                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/scope-manager (dev)       │ MIT           │ TypeScript scope analyser for ESLint                                               │
│                                              │               │ https://typescript-eslint.io/packages/scope-manager                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/tsconfig-utils (dev)      │ MIT           │ Utilities for collecting TSConfigs for linting scenarios.                          │
│                                              │               │ https://typescript-eslint.io                                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/type-utils (dev)          │ MIT           │ Type utilities for working with TypeScript + ESLint together                       │
│                                              │               │ https://typescript-eslint.io                                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/types (dev)               │ MIT           │ Types for the TypeScript-ESTree AST spec                                           │
│                                              │               │ https://typescript-eslint.io                                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/typescript-estree (dev)   │ MIT           │ A parser that converts TypeScript source code into an ESTree compatible form       │
│                                              │               │ https://typescript-eslint.io/packages/typescript-estree                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/utils (dev)               │ MIT           │ Utilities for working with TypeScript + ESLint together                            │
│                                              │               │ https://typescript-eslint.io/packages/utils                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @typescript-eslint/visitor-keys (dev)        │ MIT           │ Visitor keys used to help traverse the TypeScript-ESTree AST                       │
│                                              │               │ https://typescript-eslint.io                                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @vitejs/plugin-react (dev)                   │ MIT           │ Evan You                                                                           │
│                                              │               │ The default Vite plugin for React projects                                         │
│                                              │               │ https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-react#readme │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/accordion                            │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the accordion widget implemented as a state machine                 │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/anatomy                              │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/angle-slider                         │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the angle-slider widget implemented as a state machine              │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/aria-hidden                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Hide targets from screen readers                                                   │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/async-list                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the async-list widget implemented as a state machine                │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/auto-resize                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Autoresize utilities for the web                                                   │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/avatar                               │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the avatar widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/carousel                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the carousel widget implemented as a state machine                  │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/cascade-select                       │ MIT           │ Abraham Aremu                                                                      │
│                                              │               │ Core logic for the cascade-select widget implemented as a state machine            │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/checkbox                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the checkbox widget implemented as a state machine                  │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/clipboard                            │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the clipboard widget implemented as a state machine                 │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/collapsible                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the collapsible widget implemented as a state machine               │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/collection                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Utilities to manage a collection of items.                                         │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/color-picker                         │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the color-picker widget implemented as a state machine              │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/color-utils                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Color utilities for zag.js                                                         │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/combobox                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the combobox widget implemented as a state machine                  │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/core                                 │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ A minimal implementation of xstate fsm for UI machines                             │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/date-input                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the date-input widget implemented as a state machine                │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/date-picker                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the date-picker widget implemented as a state machine               │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/date-utils                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Date utilities for zag.js                                                          │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/dialog                               │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the dialog widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/dismissable                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Dismissable layer utilities for the DOM                                            │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/dom-query                            │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ The dom helper library for zag.js machines                                         │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/drawer                               │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the drawer widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/editable                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the editable widget implemented as a state machine                  │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/file-upload                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the file-upload widget implemented as a state machine               │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/file-utils                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ JS File API utilities                                                              │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/floating-panel                       │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the floating-panel widget implemented as a state machine            │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/focus-trap                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Focus trap utility                                                                 │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/focus-visible                        │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Focus visible polyfill utility based on WICG                                       │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/highlight-word                       │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Highlight a portion of text in a string                                            │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/hover-card                           │ MIT           │ Abraham Aremu                                                                      │
│                                              │               │ Core logic for the hover-card widget implemented as a state machine                │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/i18n-utils                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Interationalization utilities for Zag.js                                           │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/image-cropper                        │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the image-cropper widget implemented as a state machine             │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/interact-outside                     │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Track interactions or focus outside an element                                     │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/json-tree-utils                      │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Utilities for building json tree data                                              │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/listbox                              │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the listbox widget implemented as a state machine                   │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/live-region                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Implementing live region for screen readers                                        │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/marquee                              │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the marquee widget implemented as a state machine                   │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/menu                                 │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the menu widget implemented as a state machine                      │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/navigation-menu                      │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the navigation-menu widget implemented as a state machine           │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/number-input                         │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the number-input widget implemented as a state machine              │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/pagination                           │ MIT           │ Abraham Aremu                                                                      │
│                                              │               │ Core logic for the pagination widget implemented as a state machine                │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/password-input                       │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the password-input widget implemented as a state machine            │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/pin-input                            │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the pin-input widget implemented as a state machine                 │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/popover                              │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the popover widget implemented as a state machine                   │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/popper                               │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Dynamic positioning logic for ui machines                                          │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/presence                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the presence widget implemented as a state machine                  │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/progress                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the progress widget implemented as a state machine                  │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/qr-code                              │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the qr-code widget implemented as a state machine                   │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/radio-group                          │ MIT           │ Abraham Aremu                                                                      │
│                                              │               │ Core logic for the radio group widget implemented as a state machine               │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/rating-group                         │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the rating-group widget implemented as a state machine              │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/react                                │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ The react wrapper for zag                                                          │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/rect-utils                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/remove-scroll                        │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ JavaScript utility to remove scroll on body                                        │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/scroll-area                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the scroll-area widget implemented as a state machine               │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/scroll-snap                          │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Scroll snap utilities                                                              │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/select                               │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the select widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/signature-pad                        │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the signature-pad widget implemented as a state machine             │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/slider                               │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the slider widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/splitter                             │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the splitter widget implemented as a state machine                  │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/steps                                │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the steps widget implemented as a state machine                     │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/store                                │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ The reactive store package for zag machines                                        │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/switch                               │ MIT           │ Abraham Aremu                                                                      │
│                                              │               │ Core logic for the switch widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/tabs                                 │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the tabs widget implemented as a state machine                      │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/tags-input                           │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the tags-input widget implemented as a state machine                │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/timer                                │ MIT           │ Abraham Aremu                                                                      │
│                                              │               │ Core logic for the timer widget implemented as a state machine                     │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/toast                                │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the toast widget implemented as a state machine                     │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/toggle                               │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the toggle widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/toggle-group                         │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the toggle widget implemented as a state machine                    │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/tooltip                              │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the tooltip widget implemented as a state machine                   │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/tour                                 │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the tour widget implemented as a state machine                      │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/tree-view                            │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ Core logic for the tree-view widget implemented as a state machine                 │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/types                                │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ @zag-js/utils                                │ MIT           │ Segun Adebayo                                                                      │
│                                              │               │ https://github.com/chakra-ui/zag#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ acorn (dev)                                  │ MIT           │ ECMAScript parser                                                                  │
│                                              │               │ https://github.com/acornjs/acorn                                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ acorn-jsx (dev)                              │ MIT           │ Modern, fast React.js JSX parser                                                   │
│                                              │               │ https://github.com/acornjs/acorn-jsx                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ ajv (dev)                                    │ MIT           │ Evgeny Poberezkin                                                                  │
│                                              │               │ Another JSON Schema Validator                                                      │
│                                              │               │ https://github.com/ajv-validator/ajv                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ ansi-regex (dev)                             │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Regular expression for matching ANSI escape codes                                  │
│                                              │               │ https://github.com/chalk/ansi-regex#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ ansi-styles (dev)                            │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ ANSI escape codes for styling strings in the terminal                              │
│                                              │               │ https://github.com/chalk/ansi-styles#readme                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ babel-plugin-macros                          │ MIT           │ Kent C. Dodds                                                                      │
│                                              │               │ Allows you to build compile-time libraries                                         │
│                                              │               │ https://github.com/kentcdodds/babel-plugin-macros#readme                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ balanced-match (dev)                         │ MIT           │ Match balanced character pairs, like "{" and "}"                                   │
│                                              │               │ https://github.com/juliangruber/balanced-match#readme                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ brace-expansion (dev)                        │ MIT           │ Brace expansion as known from sh/bash                                              │
│                                              │               │ https://github.com/juliangruber/brace-expansion#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ browserslist (dev)                           │ MIT           │ Andrey Sitnik                                                                      │
│                                              │               │ Share target browsers between different front-end tools, like Autoprefixer,        │
│                                              │               │ Stylelint and babel-env-preset                                                     │
│                                              │               │ https://github.com/browserslist/browserslist#readme                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ callsites                                    │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Get callsites from the V8 stack trace API                                          │
│                                              │               │ https://github.com/sindresorhus/callsites#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ color-convert (dev)                          │ MIT           │ Heather Arthur                                                                     │
│                                              │               │ Plain color conversion functions                                                   │
│                                              │               │ https://github.com/Qix-/color-convert#readme                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ color-name (dev)                             │ MIT           │ DY                                                                                 │
│                                              │               │ A list of color names and its values                                               │
│                                              │               │ https://github.com/colorjs/color-name                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ convert-source-map (dev)                     │ MIT           │ Thorsten Lorenz                                                                    │
│                                              │               │ Converts a source-map from/to  different formats and allows adding/changing        │
│                                              │               │ properties.                                                                        │
│                                              │               │ https://github.com/thlorenz/convert-source-map                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ cookie                                       │ MIT           │ Roman Shtylman                                                                     │
│                                              │               │ HTTP server cookie parsing and serialization                                       │
│                                              │               │ https://github.com/jshttp/cookie#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ cosmiconfig                                  │ MIT           │ David Clark                                                                        │
│                                              │               │ Find and load configuration from a package.json property, rc file, or CommonJS     │
│                                              │               │ module                                                                             │
│                                              │               │ https://github.com/davidtheclark/cosmiconfig#readme                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ cross-spawn (dev)                            │ MIT           │ André Cruz                                                                         │
│                                              │               │ Cross platform child_process#spawn and child_process#spawnSync                     │
│                                              │               │ https://github.com/moxystudio/node-cross-spawn                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ csstype                                      │ MIT           │ Fredrik Nicol                                                                      │
│                                              │               │ Strict TypeScript and Flow types for style based on MDN data                       │
│                                              │               │ https://github.com/frenic/csstype#readme                                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ debug                                        │ MIT           │ Josh Junon                                                                         │
│                                              │               │ Lightweight debugging utility for Node.js and the browser                          │
│                                              │               │ https://github.com/debug-js/debug#readme                                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ deep-is (dev)                                │ MIT           │ Thorsten Lorenz                                                                    │
│                                              │               │ node's assert.deepEqual algorithm except for NaN being equal to NaN                │
│                                              │               │ https://github.com/thlorenz/deep-is#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ emoji-regex (dev)                            │ MIT           │ Mathias Bynens                                                                     │
│                                              │               │ A regular expression to match all Emoji-only symbols as per the Unicode Standard.  │
│                                              │               │ https://mths.be/emoji-regex                                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ enhanced-resolve (dev)                       │ MIT           │ Tobias Koppers @sokra                                                              │
│                                              │               │ Offers a async require.resolve function. It's highly configurable.                 │
│                                              │               │ http://github.com/webpack/enhanced-resolve                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ error-ex                                     │ MIT           │ Easy error subclassing and stack customization                                     │
│                                              │               │ https://github.com/qix-/node-error-ex#readme                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ es-errors                                    │ MIT           │ Jordan Harband                                                                     │
│                                              │               │ A simple cache for a few of the JS Error constructors.                             │
│                                              │               │ https://github.com/ljharb/es-errors#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ escalade (dev)                               │ MIT           │ Luke Edwards                                                                       │
│                                              │               │ A tiny (183B to 210B) and fast utility to ascend parent directories                │
│                                              │               │ https://github.com/lukeed/escalade#readme                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ escape-string-regexp                         │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Escape RegExp special characters                                                   │
│                                              │               │ https://github.com/sindresorhus/escape-string-regexp#readme                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ eslint (dev)                                 │ MIT           │ Nicholas C. Zakas                                                                  │
│                                              │               │ An AST-based pattern checker for JavaScript.                                       │
│                                              │               │ https://eslint.org                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ eslint-plugin-react-hooks (dev)              │ MIT           │ ESLint rules for React Hooks                                                       │
│                                              │               │ https://react.dev/                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ eslint-plugin-react-refresh (dev)            │ MIT           │ Arnaud Barré                                                                       │
│                                              │               │ Validate that your components can safely be updated with Fast Refresh              │
│                                              │               │ https://github.com/ArnaudBarre/eslint-plugin-react-refresh#readme                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ fast-deep-equal (dev)                        │ MIT           │ Evgeny Poberezkin                                                                  │
│                                              │               │ Fast deep equal                                                                    │
│                                              │               │ https://github.com/epoberezkin/fast-deep-equal#readme                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ fast-json-stable-stringify (dev)             │ MIT           │ James Halliday                                                                     │
│                                              │               │ deterministic `JSON.stringify()` - a faster version of substack's                  │
│                                              │               │ json-stable-strigify without jsonify                                               │
│                                              │               │ https://github.com/epoberezkin/fast-json-stable-stringify                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ fast-levenshtein (dev)                       │ MIT           │ Ramesh Nair                                                                        │
│                                              │               │ Efficient implementation of Levenshtein algorithm  with locale-specific collator   │
│                                              │               │ support.                                                                           │
│                                              │               │ https://github.com/hiddentao/fast-levenshtein#readme                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ fdir (dev)                                   │ MIT           │ thecodrr                                                                           │
│                                              │               │ The fastest directory crawler & globbing alternative to glob, fast-glob, &         │
│                                              │               │ tiny-glob. Crawls 1m files in < 1s                                                 │
│                                              │               │ https://github.com/thecodrr/fdir#readme                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ file-entry-cache (dev)                       │ MIT           │ Jared Wray                                                                         │
│                                              │               │ Super simple cache for file metadata, useful for process that work o a given       │
│                                              │               │ series of files and that only need to repeat the job on the changed ones since the │
│                                              │               │ previous run of the process                                                        │
│                                              │               │ https://github.com/jaredwray/file-entry-cache#readme                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ find-root                                    │ MIT           │ jsdnxx                                                                             │
│                                              │               │ find the closest package.json                                                      │
│                                              │               │ https://github.com/js-n/find-root#readme                                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ find-up (dev)                                │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Find a file or directory by walking up parent directories                          │
│                                              │               │ https://github.com/sindresorhus/find-up#readme                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ flat-cache (dev)                             │ MIT           │ Jared Wray                                                                         │
│                                              │               │ A stupidly simple key/value storage using files to persist some data               │
│                                              │               │ https://github.com/jaredwray/flat-cache#readme                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ function-bind                                │ MIT           │ Raynos                                                                             │
│                                              │               │ Implementation of Function.prototype.bind                                          │
│                                              │               │ https://github.com/Raynos/function-bind                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ gensync (dev)                                │ MIT           │ Logan Smyth                                                                        │
│                                              │               │ Allows users to use generators in order to write common functions that can be both │
│                                              │               │ sync or async.                                                                     │
│                                              │               │ https://github.com/loganfsmyth/gensync                                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ globals (dev)                                │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Global identifiers from different JavaScript environments                          │
│                                              │               │ https://github.com/sindresorhus/globals#readme                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ hasown                                       │ MIT           │ Jordan Harband                                                                     │
│                                              │               │ A robust, ES3 compatible, "has own property" predicate.                            │
│                                              │               │ https://github.com/inspect-js/hasOwn#readme                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ hermes-estree (dev)                          │ MIT           │ Flow types for the Flow-ESTree spec produced by the hermes parser                  │
│                                              │               │ https://github.com/facebook/hermes#readme                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ hermes-parser (dev)                          │ MIT           │ A JavaScript parser built from the Hermes engine                                   │
│                                              │               │ https://github.com/facebook/hermes#readme                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ ignore (dev)                                 │ MIT           │ kael                                                                               │
│                                              │               │ Ignore is a manager and filter for .gitignore rules, the one used by eslint,       │
│                                              │               │ gitbook and many others.                                                           │
│                                              │               │ https://github.com/kaelzhang/node-ignore#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ import-fresh                                 │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Import a module while bypassing the cache                                          │
│                                              │               │ https://github.com/sindresorhus/import-fresh#readme                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ imurmurhash (dev)                            │ MIT           │ Jens Taylor                                                                        │
│                                              │               │ An incremental implementation of MurmurHash3                                       │
│                                              │               │ https://github.com/jensyt/imurmurhash-js                                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ is-arrayish                                  │ MIT           │ Qix                                                                                │
│                                              │               │ Determines if an object can be used as an array                                    │
│                                              │               │ https://github.com/qix-/node-is-arrayish#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ is-core-module                               │ MIT           │ Jordan Harband                                                                     │
│                                              │               │ Is this specifier a node.js core module?                                           │
│                                              │               │ https://github.com/inspect-js/is-core-module                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ is-extglob (dev)                             │ MIT           │ Jon Schlinkert                                                                     │
│                                              │               │ Returns true if a string has an extglob.                                           │
│                                              │               │ https://github.com/jonschlinkert/is-extglob                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ is-fullwidth-code-point (dev)                │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Check if the character represented by a given Unicode code point is fullwidth      │
│                                              │               │ https://github.com/sindresorhus/is-fullwidth-code-point#readme                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ is-glob (dev)                                │ MIT           │ Jon Schlinkert                                                                     │
│                                              │               │ Returns `true` if the given string looks like a glob pattern or an extglob         │
│                                              │               │ pattern. This makes it easy to create code that only uses external modules like    │
│                                              │               │ node-glob when necessary, resulting in much faster code execution and              │
│                                              │               │ initialization time, and a better user experience.                                 │
│                                              │               │ https://github.com/micromatch/is-glob                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ jiti (dev)                                   │ MIT           │ Runtime typescript and ESM support for Node.js                                     │
│                                              │               │ https://github.com/unjs/jiti#readme                                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ js-tokens                                    │ MIT           │ Simon Lydell                                                                       │
│                                              │               │ A regex that tokenizes JavaScript.                                                 │
│                                              │               │ https://github.com/lydell/js-tokens#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ jsesc                                        │ MIT           │ Mathias Bynens                                                                     │
│                                              │               │ Given some data, jsesc returns the shortest possible stringified & ASCII-safe      │
│                                              │               │ representation of that data.                                                       │
│                                              │               │ https://mths.be/jsesc                                                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ json-buffer (dev)                            │ MIT           │ Dominic Tarr                                                                       │
│                                              │               │ JSON parse & stringify that supports binary via bops & base64                      │
│                                              │               │ https://github.com/dominictarr/json-buffer                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ json-parse-even-better-errors                │ MIT           │ Kat Marchán                                                                        │
│                                              │               │ JSON.parse with context information on error                                       │
│                                              │               │ https://github.com/npm/json-parse-even-better-errors#readme                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ json-schema-traverse (dev)                   │ MIT           │ Evgeny Poberezkin                                                                  │
│                                              │               │ Traverse JSON Schema passing each schema object to callback                        │
│                                              │               │ https://github.com/epoberezkin/json-schema-traverse#readme                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ json-stable-stringify-without-jsonify (dev)  │ MIT           │ James Halliday                                                                     │
│                                              │               │ deterministic JSON.stringify() with custom sorting to get deterministic hashes     │
│                                              │               │ from stringified results, with no public domain dependencies                       │
│                                              │               │ https://github.com/samn/json-stable-stringify                                      │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ json5 (dev)                                  │ MIT           │ Aseem Kishore                                                                      │
│                                              │               │ JSON for Humans                                                                    │
│                                              │               │ http://json5.org/                                                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ keyv (dev)                                   │ MIT           │ Jared Wray                                                                         │
│                                              │               │ Simple key-value storage with support for multiple backends                        │
│                                              │               │ https://github.com/jaredwray/keyv                                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ levn (dev)                                   │ MIT           │ George Zahariev                                                                    │
│                                              │               │ Light ECMAScript (JavaScript) Value Notation - human written, concise, typed,      │
│                                              │               │ flexible                                                                           │
│                                              │               │ https://github.com/gkz/levn                                                        │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ lines-and-columns                            │ MIT           │ Brian Donovan                                                                      │
│                                              │               │ Maps lines and columns to character offsets and back.                              │
│                                              │               │ https://github.com/eventualbuddha/lines-and-columns#readme                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ locate-path (dev)                            │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Get the first path that exists on disk of multiple paths                           │
│                                              │               │ https://github.com/sindresorhus/locate-path#readme                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ magic-string (dev)                           │ MIT           │ Rich Harris                                                                        │
│                                              │               │ Modify strings, generate sourcemaps                                                │
│                                              │               │ https://github.com/Rich-Harris/magic-string#readme                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ ms                                           │ MIT           │ Tiny millisecond conversion utility                                                │
│                                              │               │ https://github.com/vercel/ms#readme                                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ nanoid (dev)                                 │ MIT           │ Andrey Sitnik                                                                      │
│                                              │               │ A tiny (116 bytes), secure URL-friendly unique string ID generator                 │
│                                              │               │ https://github.com/ai/nanoid#readme                                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ natural-compare (dev)                        │ MIT           │ Lauri Rooden                                                                       │
│                                              │               │ Compare strings containing a mix of letters and numbers in the way a human being   │
│                                              │               │ would in sort order.                                                               │
│                                              │               │ https://github.com/litejs/natural-compare-lite#readme                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ next-themes                                  │ MIT           │ https://github.com/pacocoursey/next-themes#readme                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ node-releases (dev)                          │ MIT           │ Sergey Rubanov                                                                     │
│                                              │               │ Node.js releases data                                                              │
│                                              │               │ https://github.com/chicoxyzzy/node-releases#readme                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ optionator (dev)                             │ MIT           │ George Zahariev                                                                    │
│                                              │               │ option parsing and help generation                                                 │
│                                              │               │ https://github.com/gkz/optionator                                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ p-limit (dev)                                │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Run multiple promise-returning & async functions with limited concurrency          │
│                                              │               │ https://github.com/sindresorhus/p-limit#readme                                     │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ p-locate (dev)                               │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Get the first fulfilled promise that satisfies the provided testing function       │
│                                              │               │ https://github.com/sindresorhus/p-locate#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ p-try (dev)                                  │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ `Start a promise chain                                                             │
│                                              │               │ https://github.com/sindresorhus/p-try#readme                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ parent-module                                │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Get the path of the parent module                                                  │
│                                              │               │ https://github.com/sindresorhus/parent-module#readme                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ parse-json                                   │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Parse JSON with more helpful errors                                                │
│                                              │               │ https://github.com/sindresorhus/parse-json#readme                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ path-exists (dev)                            │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Check if a path exists                                                             │
│                                              │               │ https://github.com/sindresorhus/path-exists#readme                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ path-key (dev)                               │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Get the PATH environment variable key cross-platform                               │
│                                              │               │ https://github.com/sindresorhus/path-key#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ path-parse                                   │ MIT           │ Javier Blanco                                                                      │
│                                              │               │ Node.js path.parse() ponyfill                                                      │
│                                              │               │ https://github.com/jbgutierrez/path-parse#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ path-type                                    │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Check if a path is a file, directory, or symlink                                   │
│                                              │               │ https://github.com/sindresorhus/path-type#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ perfect-freehand                             │ MIT           │ Steve Ruiz                                                                         │
│                                              │               │ Draw perfect pressure-sensitive freehand strokes.                                  │
│                                              │               │ https://github.com/steveruizok/perfect-freehand#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ picomatch (dev)                              │ MIT           │ Jon Schlinkert                                                                     │
│                                              │               │ Blazing fast and accurate glob matcher written in JavaScript, with no dependencies │
│                                              │               │ and full support for standard and extended Bash glob features, including braces,   │
│                                              │               │ extglobs, POSIX brackets, and regular expressions.                                 │
│                                              │               │ https://github.com/micromatch/picomatch                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ postcss (dev)                                │ MIT           │ Andrey Sitnik                                                                      │
│                                              │               │ Tool for transforming styles with JS plugins                                       │
│                                              │               │ https://postcss.org/                                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ prelude-ls (dev)                             │ MIT           │ George Zahariev                                                                    │
│                                              │               │ prelude.ls is a functionally oriented utility library. It is powerful and          │
│                                              │               │ flexible. Almost all of its functions are curried. It is written in, and is the    │
│                                              │               │ recommended base library for, LiveScript.                                          │
│                                              │               │ http://preludels.com                                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ proxy-compare                                │ MIT           │ Daishi Kato                                                                        │
│                                              │               │ Compare two objects using accessed properties with Proxy                           │
│                                              │               │ https://github.com/dai-shi/proxy-compare#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ proxy-memoize                                │ MIT           │ Daishi Kato                                                                        │
│                                              │               │ Intuitive magical memoization library with Proxy and WeakMap                       │
│                                              │               │ https://github.com/dai-shi/proxy-memoize#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ punycode (dev)                               │ MIT           │ Mathias Bynens                                                                     │
│                                              │               │ A robust Punycode converter that fully complies to RFC 3492 and RFC 5891, and      │
│                                              │               │ works on nearly all JavaScript platforms.                                          │
│                                              │               │ https://mths.be/punycode                                                           │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ react                                        │ MIT           │ React is a JavaScript library for building user interfaces.                        │
│                                              │               │ https://react.dev/                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ react-dom                                    │ MIT           │ React package for working with the DOM.                                            │
│                                              │               │ https://react.dev/                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ react-error-boundary                         │ MIT           │ Brian Vaughn                                                                       │
│                                              │               │ Simple reusable React error boundary component                                     │
│                                              │               │ https://react-error-boundary-lib.vercel.app/                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ react-icons                                  │ MIT           │ Goran Gajic                                                                        │
│                                              │               │ SVG React icons of popular icon packs using ES6 imports                            │
│                                              │               │ https://github.com/react-icons/react-icons#readme                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ react-is                                     │ MIT           │ Brand checking of React Elements.                                                  │
│                                              │               │ https://reactjs.org/                                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ react-router                                 │ MIT           │ Remix Software                                                                     │
│                                              │               │ Declarative routing for React                                                      │
│                                              │               │ https://github.com/remix-run/react-router#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ react-router-dom                             │ MIT           │ Remix Software                                                                     │
│                                              │               │ Declarative routing for React web applications                                     │
│                                              │               │ https://github.com/remix-run/react-router#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ resolve                                      │ MIT           │ James Halliday                                                                     │
│                                              │               │ resolve like require.resolve() on behalf of files asynchronously and synchronously │
│                                              │               │ https://github.com/browserify/resolve#readme                                       │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ resolve-from                                 │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Resolve the path of a module like `require.resolve()` but from a given path        │
│                                              │               │ https://github.com/sindresorhus/resolve-from#readme                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ rolldown (dev)                               │ MIT           │ Fast JavaScript/TypeScript bundler in Rust with Rollup-compatible API.             │
│                                              │               │ https://rolldown.rs/                                                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ scheduler                                    │ MIT           │ Cooperative scheduler for the browser environment.                                 │
│                                              │               │ https://react.dev/                                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ set-cookie-parser                            │ MIT           │ Nathan Friedly                                                                     │
│                                              │               │ Parses set-cookie headers into objects                                             │
│                                              │               │ https://github.com/nfriedly/set-cookie-parser                                      │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ shebang-command (dev)                        │ MIT           │ Kevin Mårtensson                                                                   │
│                                              │               │ Get the command from a shebang                                                     │
│                                              │               │ https://github.com/kevva/shebang-command#readme                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ shebang-regex (dev)                          │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Regular expression for matching a shebang line                                     │
│                                              │               │ https://github.com/sindresorhus/shebang-regex#readme                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ string-width (dev)                           │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Get the visual width of a string - the number of columns required to display it    │
│                                              │               │ https://github.com/sindresorhus/string-width#readme                                │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ strip-ansi (dev)                             │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Strip ANSI escape codes from a string                                              │
│                                              │               │ https://github.com/chalk/strip-ansi#readme                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ stylis                                       │ MIT           │ Sultan Tarimo                                                                      │
│                                              │               │ A Light–weight CSS Preprocessor                                                    │
│                                              │               │ https://github.com/thysultan/stylis.js                                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ supports-preserve-symlinks-flag              │ MIT           │ Jordan Harband                                                                     │
│                                              │               │ Determine if the current node version supports the `--preserve-symlinks` flag.     │
│                                              │               │ https://github.com/inspect-js/node-supports-preserve-symlinks-flag#readme          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ tailwindcss (dev)                            │ MIT           │ A utility-first CSS framework for rapidly building custom user interfaces.         │
│                                              │               │ https://tailwindcss.com                                                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ tapable (dev)                                │ MIT           │ Tobias Koppers @sokra                                                              │
│                                              │               │ Just a little module for plugins.                                                  │
│                                              │               │ https://github.com/webpack/tapable                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ tinyglobby (dev)                             │ MIT           │ Superchupu                                                                         │
│                                              │               │ A fast and minimal alternative to globby and fast-glob                             │
│                                              │               │ https://superchupu.dev/tinyglobby                                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ ts-api-utils (dev)                           │ MIT           │ JoshuaKGoldberg                                                                    │
│                                              │               │ Utility functions for working with TypeScript's API. Successor to the wonderful    │
│                                              │               │ tsutils. 🛠️️
h                                                                      │
│                                              │               │                                                                                    │
│                                              │               │ tps://github.com/JoshuaKGoldberg/ts-api-utils#readme                               │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ type-check (dev)                             │ MIT           │ George Zahariev                                                                    │
│                                              │               │ type-check allows you to check the types of JavaScript values at runtime with a    │
│                                              │               │ Haskell like type syntax.                                                          │
│                                              │               │ https://github.com/gkz/type-check                                                  │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ typescript-eslint (dev)                      │ MIT           │ Tooling which enables you to use TypeScript with ESLint                            │
│                                              │               │ https://typescript-eslint.io/packages/typescript-eslint                            │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ undici-types (dev)                           │ MIT           │ A stand-alone types package for Undici                                             │
│                                              │               │ https://undici.nodejs.org                                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ update-browserslist-db (dev)                 │ MIT           │ Andrey Sitnik                                                                      │
│                                              │               │ CLI tool to update caniuse-lite to refresh target browsers from Browserslist       │
│                                              │               │ config                                                                             │
│                                              │               │ https://github.com/browserslist/update-db#readme                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ uqr                                          │ MIT           │ Anthony Fu                                                                         │
│                                              │               │ Generate QR Code universally, in any runtime, to ANSI, Unicode or SVG.             │
│                                              │               │ https://github.com/unjs/uqr#readme                                                 │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ vite (dev)                                   │ MIT           │ Evan You                                                                           │
│                                              │               │ Native-ESM powered web dev build tool                                              │
│                                              │               │ https://vite.dev                                                                   │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ word-wrap (dev)                              │ MIT           │ Jon Schlinkert                                                                     │
│                                              │               │ Wrap words to a specified length.                                                  │
│                                              │               │ https://github.com/jonschlinkert/word-wrap                                         │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ wrap-ansi (dev)                              │ MIT           │ Sindre Sorhus                                                                      │
│                                              │               │ Wordwrap a string with ANSI escape codes                                           │
│                                              │               │ https://github.com/chalk/wrap-ansi#readme                                          │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ zod (dev)                                    │ MIT           │ Colin McDonnell                                                                    │
│                                              │               │ TypeScript-first schema declaration and validation library with static type        │
│                                              │               │ inference                                                                          │
│                                              │               │ https://zod.dev                                                                    │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ zod-validation-error (dev)                   │ MIT           │ Dimitrios C. Michalakos                                                            │
│                                              │               │ Wrap zod validation errors in user-friendly readable messages                      │
│                                              │               │ https://github.com/causaly/zod-validation-error#readme                             │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ lightningcss (dev)                           │ MPL-2.0       │ A CSS parser, transformer, and minifier written in Rust                            │
│                                              │               │ https://github.com/parcel-bundler/lightningcss#readme                              │
├──────────────────────────────────────────────┼───────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ lightningcss-linux-x64-gnu (dev)             │ MPL-2.0       │ A CSS parser, transformer, and minifier written in Rust                            │
│                                              │               │ https://github.com/parcel-bundler/lightningcss#readme                              │
└──────────────────────────────────────────────┴───────────────┴────────────────────────────────────────────────────────────────────────────────────┘
