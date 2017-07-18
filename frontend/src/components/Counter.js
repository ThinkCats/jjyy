import React from 'react';
import  {Component} from 'reflux';
import  { Button} from 'antd';
import TestStore from 'stores/TestStore';
import TestAction from 'actions/TestAction';


export default class World extends Component {

    constructor(props) {
        super(props);
        this.stores = [TestStore];
    }

    hanldeOK = () => {
        console.log('hello');
        console.log('count state:',this.state.counter);
    }

    render() {
        return (
            <div>
                <h1 onClick={this.hanldeOK}>Counter Example!</h1>
                <div>
                    <h2> current counter: {this.state.counter}</h2>
                </div>
                <Operate />
            </div>
        );
    }
}

class Operate extends Component {
    render() {
        return (
            <div>
                <Button onClick={() => TestAction.increment()}>increment</Button>
                <Button onClick={() => TestAction.decrement(2)}>decrement 2</Button>
            </div>
        )
    }
}
