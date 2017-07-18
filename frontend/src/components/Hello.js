import React, {Component} from 'react';
import {Link} from  'react-router-dom';
import  {notification, Button} from 'antd';

class Hello extends Component {

    render() {
        return (
            <div>
                <h1>Hello world !</h1>
                <Operate />
            </div>
        )
    }
}

export default (Hello);

const Operate = () => (
    <div>
        <div>
            <Link to="/world">Counter</Link>
        </div>
        <br/>
        <Button onClick={() => notification.open({message:'hello'})}>Notify</Button>
    </div>
);
