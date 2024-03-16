const path = require('path');

module.exports = {
    mode: 'development',
    entry: './frontend/src/index.js', // Entry point of your application
    output: {
        path: path.resolve(__dirname, 'dist'), // Output directory
        filename: 'bundle.js', // Output bundle name
    },
    module: {
        rules: [
        {
            test: /\.(js|jsx)$/,
            exclude: /node_modules/,
            use: {
            loader: 'babel-loader',
            options: {
                presets: ['@babel/preset-react'], // Enable JSX transformation
                plugins: [
                    ['@babel/plugin-transform-react-jsx', { throwIfNamespace: false }]
                ]
            },
            },
        },
        ],
    },
    };
