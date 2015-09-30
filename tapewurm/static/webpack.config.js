var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: './src/main.js',
  output: { path: __dirname + '/build', filename: 'bundle.js' },
  module: {
    loaders: [
      { test: /.jsx?$/, loader: 'babel-loader', exclude: /node_modules/ }
    ]
  },
};