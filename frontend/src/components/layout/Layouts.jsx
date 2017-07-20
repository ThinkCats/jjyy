import React, {Component} from 'react';
import {Layout} from 'antd';
import Header from 'components/layout/Header';

const { Footer,Sider } = Layout;

const Footers = ()  => (
  <div>
    <Footer style={{ textAlign: 'center' }}>
      Ant Design ©2016 Created by Ant UED
    </Footer>
  </div>
);

class Layouts extends Component {
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
        )
    }
}


export default Layouts;
