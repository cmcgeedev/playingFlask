import React from 'react';
import { connect } from 'react-redux';
import { getTableContacts } from '../selectors';
import ContactRow from './ContactRow';
import ContactDetailRow from './ContactDetailRow';
import TableHeader from './TableHeader';
import '../style/contact-table';

export class ContactTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      showDetail: false
    };
  }

  render() {
    let contacts = this.props.contacts;

    let rows = contacts.map((contact) => <ContactRow key={'contact-' + contact.zuid} contact={contact} readOnly={this.props.readOnly} rowStyle={this.props.rowStyle} /> );

    if (this.props.detailContact) {
      const contactRow = contacts.findIndex((contact) => contact.zuid === this.props.detailContact);
      if (contactRow !== -1) {
        rows.splice(contactRow + 1, 0, <ContactDetailRow key='contact-detail' contact={contacts[contactRow]} readOnly={this.props.rowStyle==='readonly'} />);
      }
    }

    if (contacts.length === 0) {
      rows = (
        <tr>
          <td colSpan="6">
            <div className="slds-m-around--medium slds-align--absolute-center">
              No contacts
            </div>
          </td>
        </tr>
      );
    }

    return (
      <table className='contact-table slds-table slds-table--bordered slds-table--cell-buffer slds-table--striped slds-no-row-hover'>
        <TableHeader rowStyle={this.props.rowStyle} />
        <tbody>
          {rows}
        </tbody>
      </table>
    );
  }
}

export const mapStateToProps = (state, ownProps) => {
  return {
    contacts: getTableContacts(state),
    contactLimit: (ownProps.list === null) ? 10 : undefined,
    readOnly: ownProps.readOnly || false,
    rowStyle: ownProps.rowStyle,
    detailContact: state.ui.detailContact
  };
};

export default connect(mapStateToProps)(ContactTable);

const prospectMapStateToProps = (state) => {
  return {
    contacts: getTableContacts(state),
    detailContact: state.ui.detailContact,
    rowStyle: 'lockable'
  };
};

export const ProspectsTable = connect(prospectMapStateToProps)(ContactTable);