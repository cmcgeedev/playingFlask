import React from 'react'
import { connect } from 'react-redux';
import { withRouter } from 'react-router';
import { userLogin } from '../actions';
import LoginForm from './loginForm';
import SiteHeader from './siteHeader';
import { NetworkErrorBar } from './ErrorBar'

export class SearchPetsPage extends React.Component {
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
        this.props.searchRequest({
        'breed':this.state.breed,
        'city': this.state.city,
        'max_weight': this.state.max_weight,
        'min_weight': this.state.min_weight,
        'max_age': this.state.max_age,
        'min_age': this.state.min_age,
        'species': this.state.species
        });
    }

    render() {
    return (
      <div className='upload-form slds-is-relative'>
          <form className='slds-form--inline' onSubmit={this.onSubmit}>
            <div className='slds-form-element'>
              <div className='slds-form-element__label'>Breed:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='breed' value={this.state.input} onChange={this.onInput} required />
              </div>
              <div className='slds-form-element__label'>City:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='city' value={this.state.input} onChange={this.onInput} required />
              </div>
              <div className='slds-form-element__label'>Maximum Weight:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='max_weight' value={this.state.input} onChange={this.onInput} required />
              </div>
              <div className='slds-form-element__label'>Minimum Weight:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='min_weight' value={this.state.input} onChange={this.onInput} required />
              </div>
              <div className='slds-form-element__label'>Maximum Age:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='max_age' value={this.state.input} onChange={this.onInput} required />
              </div>
              <div className='slds-form-element__label'>Minimum Age:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='min_age' value={this.state.input} onChange={this.onInput} required />
              </div>
              <div className='slds-form-element__label'>Species:</div>
              <div className='slds-form-element__control'>
                <input className='slds-input' type='text' name='species' value={this.state.input} onChange={this.onInput} required />
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
  searchRequest: (data) => { dispatch(searchPets(data)); },
});

const mapStateToProps = (state) => ({

});

export default connect(mapStateToProps, mapDispatchToProps)(SearchPetsPage);