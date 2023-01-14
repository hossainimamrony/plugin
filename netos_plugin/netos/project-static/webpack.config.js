const path = require('path');

var softwareEolConfig = (env) => ({
  entry: './src/software_eol.ts',
  mode: env.production ? 'production' : 'development',
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
  output: {
    filename: 'software_eol.js',
    path: path.resolve(__dirname, 'dist'),
  },
})


module.exports = (env) => [
  softwareEolConfig(env)
];

