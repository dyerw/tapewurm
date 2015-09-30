import React from 'react';
import { TrackEditor } from './trackeditor.jsx'

class MixMaker extends React.Component {

  constructor(){
    super();

    this.state = {
      name: '',
      // Begins with an empty track editor
      tracks: [{order: 1, musicbrainz_id: null,
                title: "", note: ""}],
      image_url: ''
    };
  }

  render() {
    console.log("rendering");

    // Create an array of all the track editors
    let trackEditors = [];
    for (let track of this.state.tracks) {
      trackEditors.push(<TrackEditor key={track.order} order={track.order} title={track.title}
                               note={track.note} updateFunction={this.trackUpdated} />);
    }

    return (
      <div id="mix-maker">

        {/* Mix Image Editor */}
        <div id="mix-image-preview">
          <img src={this.state.image_url != '' ?
                    this.state.image_url : 'default_img.jpg'} />
          <input type="text" placeholder="Image URL" value={this.state.image_url}
                 onChange={e => this.setState({image_url: e.target.value})} />
        </div>

        {/* Mix Name Editor */}
        <div id="mix-name-editor">
          <input type="text" value={this.state.name} placeholder="Mix name"
                 onChange={e => this.setState({name: e.target.value})} />
        </div>

        {/* Track Editors */}
        {trackEditors}

        {/* Add Track Button */}
        <button onClick={this.addTrack}> + </button>

        {/* Create Button */}
        <button onClick={this.createMix}>Create</button>

      </div>
    );
  }

  // Behaviors

  /*
   * Adds an empty new track editor at the bottom of the mix.
   */
  addTrack() {
  }

  /*
   * Sends all mix info up to server and then provides a link
   * to the newly created mix.
   */
  createMix() {
  }

  /*
   * Fired off whenever the user edits a track.
   */
  trackUpdated(trackOrder) {
  }
}

React.render(<MixMaker/>, document.body);
