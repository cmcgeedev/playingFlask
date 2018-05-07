import React from 'react';
import { render } from 'react-dom';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import thunkMiddleware from 'redux-thunk';
import URLSearchParams from 'url-search-params';
import { Router, Route, IndexRoute, Redirect, hashHistory } from 'react-router';


let store = createStore(reducer, applyMiddleware(thunkMiddleware));

document.addEventListener('DOMContentLoaded', () => {
    render({
        <Provider store=(store)>
            <Router history={hashHistory}>

    })
});