import React from 'react';
import { connect } from 'react-redux';
import { clearNetworkError } from '../actions';
import { getIcon } from '../util';

export class ErrorBar extends React.Component {
  render() {
    if (this.props.error) {
      const message = (this.props.message)
        ? this.props.message
        : this.props.error.message;

      return (
        <div className='slds-notify-container'>
          <div className="slds-notify slds-notify--alert slds-notify--toast slds-theme--error slds-theme--alert-texture" role="alert">
            <button className="slds-button slds-notify__close slds-button--icon-inverse" onClick={this.props.close}>
              <svg aria-hidden="true" className="slds-button__icon">
                <use xlinkHref={getIcon('utility-sprite/svg/symbols.svg#close')}></use>
              </svg>
              <span className="slds-assistive-text">Close</span>
            </button>
            <h2>
              <svg aria-hidden="true" className="slds-icon slds-icon--small slds-m-right--x-small">
                <use xlinkHref={getIcon('utility-sprite/svg/symbols.svg#ban')}></use>
              </svg>
              {message}
            </h2>
          </div>
        </div>
      );
    } else {
      return null;
    }
  }
}

const mapStateToProps = (state, ownProps) => ({
  ...ownProps,
  error: state.network.error
});

const mapDispatchToProps = (dispatch) => ({
  close: () => dispatch(clearNetworkError())
});

export const NetworkErrorBar = connect(mapStateToProps, mapDispatchToProps)(ErrorBar);