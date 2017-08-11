// Generated by CoffeeScript 2.0.0-beta4
var Footer, Footers, Layouts, Sider;

import React, {
  Component
} from 'react';

import {
  Layout
} from 'antd';

import Header from 'components/layout/Header';

({Footer, Sider} = Layout);

Footers = function() {
  return (<div>
    <Footer style={{ textAlign: 'center' }}>
      Ant Design ©2016 Created by Ant UED
    </Footer>
  </div>);
};

Layouts = class Layouts extends Component {
  render() {
    return (
          <div style={{maxWidth: '1080px', margin: '0 auto'}}>
            <div className="head"><Header/></div>
            <div>
              <div className="main">{this.props.children}</div>
              <div className="sider">sider</div>
            </div>
            <div className="foot"><Footers /></div>
          </div>
        );
  }

};

export default Layouts;
