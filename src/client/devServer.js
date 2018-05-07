/* eslint-env node */

const express = require('express');
const bodyParser = require('body-parser');
const multer = require('multer');
const urlencode = require('urlencode');
const webpack = require('webpack');
const webpackDevMiddleware = require('webpack-dev-middleware');
const webpackHotMiddleware = require('webpack-hot-middleware');


const app = express();
const router = express.Router();

app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded());