import React from 'react';
import { connect } from 'react-redux';
import { callContact, deselectContact } from '../actions';
import { getIcon } from '../util';

export class PetInfoCard extends React.Component {
  render() {
    const talkingPoints = this.props.contact.talkingPoints.map(
      (talkingPoint, i) => <li style={styles} key={`item-${i}`} className='slds-item'>{talkingPoint}</li>
    );

    const styles = {
      whiteSpace: 'normal !important'
    };

    const rowClass = (this.props.contact.locked) ? 'slds-theme--alert-texture' : '';

    return (
      <tr className={rowClass}>
        <td colSpan='6'>
          <div className='slds-grid slds-m-bottom--medium'>
            <div className='slds-col'>
              <div className='slds-text-heading--medium'>{this.props.contact.pet_name}</div>
            </div>
            {/*actions*/}
            <div className='slds-col slds-text-align--right'>
              <button className='slds-button slds-button--icon'>
                <svg className='slds-button__icon' onClick={this.props.closeDetail}>
                  <use xlinkHref={getIcon('utility-sprite/svg/symbols.svg#close')}></use>
                </svg>
              </button>
            </div>
          </div>
          <div className='slds-grid slds-m-bottom--medium'>
            <div className='slds-col'>
              <div className='slds-list--horizontal slds-wrap'>
                <div className='slds-item--label slds-text-color--weak'>Age:</div>
                <div className='slds-item--detail'>{this.props.pet.age}</div>
                <div className='slds-item--label slds-text-color--weak'>Weight:</div>
                <div className='slds-item--detail'>{this.props.pet.weight}</div>
                <div className='slds-item--label slds-text-color--weak'>Breed:</div>
                <div className='slds-item--detail'>{this.props.pet.breed}</div>
              </div>
            </div>
            <div className='slds-col'>
              <div className='slds-text-title'>Talking Points</div>
              <ul className='slds-has-dividers--top'>
                {talkingPoints}
              </ul>
            </div>
          </div>
        </td>
      </tr>
    );
  }
}

const mapDispatchToProps = (dispatch) => ({
  callContact: (id) => dispatch(callContact(id)),
  closeDetail: () => dispatch(deselectContact())
});

export default connect(null, mapDispatchToProps)(ContactDetailRow);