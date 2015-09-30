import React from 'react';

class MixMaker extends React.Component {

  constructor(){
    super();

    this.state = {
      name: '',
      tracks: [],
      image_url: ''
    };
  }

  render() {
    console.log("rendering");
    return (
      <div id="mix-maker">

        {/* Mix Image Editor */}
        <div id="mix-image-preview">
          <img src={this.state.image_url != '' ?
                    this.state.image_url : 'default_img.jpg'} />
          <input type="text" placeholder="Image URL" value={this.state.image_url}
                 onChange={e => this.setState({image_url: e.target.value})}/>
        </div>

        {/* Mix Name Editor */}

      </div>
    );
  }
}

React.render(<MixMaker/>, document.body);
