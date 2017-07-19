import React from 'react';
import { Menu, Icon, Avatar } from 'antd';
const SubMenu = Menu.SubMenu;
const MenuItemGroup = Menu.ItemGroup;

class Header extends React.Component {
state = {
    current: 'mail',
  }
  handleClick = (e) => {
    this.setState({
      current: e.key,
    });
  }
  render() {
    return (
      <div style={{position: 'relative'}}>
        <Menu
          onClick={this.handleClick}
          selectedKeys={[this.state.current]}
          mode="horizontal"
          >
          <Menu.Item key="mail">
            <Icon type="mail" />One
          </Menu.Item>
          <Menu.Item key="app" >
            <Icon type="appstore" />Two
          </Menu.Item>
          <SubMenu title={<span><Icon type="setting" />Three</span>}>
            <MenuItemGroup title="Item 1">
              <Menu.Item key="setting:1">Option 1</Menu.Item>
              <Menu.Item key="setting:2">Option 2</Menu.Item>
            </MenuItemGroup>
            <MenuItemGroup title="Item 2">
              <Menu.Item key="setting:3">Option 3</Menu.Item>
              <Menu.Item key="setting:4">Option 4</Menu.Item>
            </MenuItemGroup>
          </SubMenu>
          <Menu.Item key="alipay">
            Four
          </Menu.Item>
        </Menu>
        <div className="right-section" style={{float:'right',top:'8px',right:  '2rem',position: 'absolute' }}>
          <Avatar shape="square" style={{ backgroundColor: '' }} icon="user" />
        </div>
      </div>
    );
  }
}

export default Header;
