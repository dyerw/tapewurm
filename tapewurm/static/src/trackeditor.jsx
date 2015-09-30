import React from 'react';

export class TrackEditor extends React.Component {
  render() {
    return (
      <div className="track-editor">
        <div className="track-upper-row">
          <span className="track-order">{this.props.order}</span>
          <input type="text" placeholder="Enter track name" value={this.props.name} />
        </div>
        <div className="track-bottom-row">
          <input type="text" placeholder="Enter note" value={this.props.note} />
        </div>
      </div>
    );
  }
}
