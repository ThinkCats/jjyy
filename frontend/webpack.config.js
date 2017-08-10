var path = require('path');

const theme_config = require(path.resolve(__dirname, './theme.js'));
const theme = JSON.stringify(theme_config())

var config = {
    entry: path.resolve(__dirname, 'dist/main.js'),
    output: {
        path: path.resolve(__dirname, 'build'),
        filename: 'bundle.js'
    },
    resolve: {
        extensions: ['.js', '.jsx'],
        alias: {
            'actions': path.resolve(__dirname, './dist/flux/actions'),
            'stores': path.resolve(__dirname, './dist/flux/stores'),
            'components': path.resolve(__dirname, './dist/components'),
            'services': path.resolve(__dirname, './dist/services')
        }
    },
    module: {
        loaders: [{
            test: /\.(js|jsx)?$/,
            exclude: /node_modules/,
            use: {
                loader: 'babel-loader?presets[]=es2015,presets[]=react,presets[]=stage-0',
                options: {
                    presets: ['es2015', 'react', 'stage-0'],
                    plugins: ['transform-class-properties', ['import', {
                        "libraryName": 'antd',
                        "style": true
                    }]]
                }
            },
        }, {
            test: /\.css$/, // Only .css files
            loaders: ['style-loader', 'css-loader'] // Run both loaders
        }, {
            test: /\.less$/,
            loaders: ['style-loader', 'css-loader', 'less-loader?{"modifyVars":' + theme + '}'] // Run both loaders
        }],
    }
};


module.exports = config;
