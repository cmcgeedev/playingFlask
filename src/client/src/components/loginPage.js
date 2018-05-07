import React from 'react'
import { connect } from 'react-redux';
import { withRouter } from 'react-router';
import { userLogin } from '../actions';
import LoginForm from './loginForm';
import SiteHeader from './siteHeader';
import { NetworkErrorBar } from './ErrorBar'

export class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.nextPage = this.nextPage.bind(this);

    }

    componentDidMount(){

    }

    nextPage(){
        this.props.router.push('/users/home');
    }

    render(){
        return(
            <div className='login-page'>
                <SiteHeader />
                <LoginForm />
                <NetworkErrorBar />
        );
    }
}

const mapStateToProps = (state) => ({
    selectedList: state.ui.
})