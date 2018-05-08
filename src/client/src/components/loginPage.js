import React from 'react'
import { connect } from 'react-redux';
import { withRouter } from 'react-router';
import { userLogin } from '../actions';
import LoginForm from './loginForm';
import SiteHeader from './siteHeader';
import { NetworkErrorBar } from './ErrorBar'

export class LoginPage extends React.Component {
    constructor(props) {
        this.state = { uploading: false, input: props.message };
        this.onInput = this.onInput.bind(this);
        this.onSubmit = this.onSubmit.bind(this);

    }

    componentDidMount(){

    }

    nextPage(){
        this.props.router.push('/users/home');
    }

    onInput(event) {
        this.setState({ [event.target.name]: event.target.value });
    }

    onSubmit() {
        this.setState({ uploading: true });
        this.props.loginRequest({'username':this.state.username, 'password': this.state.password});
    }

    render() {
    return (
      <div className='upload-form slds-is-relative'>
          <form className='slds-form--inline' onSubmit={this.onSubmit}>
            <div className='slds-form-element'>
              <div className='slds-form-element__label'>Username:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='username' value={this.state.input} onChange={this.onInput} required />
              </div>
              <div className='slds-form-element__label'>Password:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='password' value={this.state.input} onChange={this.onInput} required />
              </div>
            </div>
            <div className='slds-form-element__control'>
                <button className='slds-button slds-button--brand' type='submit'>Save</button>
              </div>
          </form>
      </div>
    );
  }
}

const mapDispatchToProps = (dispatch) => ({
  loginRequest: (data) => { dispatch(userLogin(data)); },
});

const mapStateToProps = (state) => ({

});

export default connect(mapStateToProps, mapDispatchToProps)(LoginPage);
