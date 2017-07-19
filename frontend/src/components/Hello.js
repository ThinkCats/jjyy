import React, {Component} from 'react';
import {Link} from  'react-router-dom';
import  {notification, Button,Row,Col} from 'antd';
import Layouts from 'components/layout/Layouts';

class Hello extends Component {
    render() {
        return (
          <Layouts>
            <div>
              <div>
                <Item />
                <Item />
                <Item />
              </div>
              <h1>Hello world !</h1>
              <Operate />
            </div>
          </Layouts>
        )
    }
}

export default (Hello);

const Item = (data) => {
  return (
    <Row>
      <Col>ttt</Col>
      <Col>yyyyy</Col>
    </Row>
  )
}


const Operate = () => (
    <div>
        <div>
            <Link to="/world">Counter</Link>
        </div>
        <br/>
        <Button onClick={() => notification.open({message:'hello'})}>Notify</Button>
    </div>
);
