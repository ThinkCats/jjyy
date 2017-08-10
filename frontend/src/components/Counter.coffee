import React from 'react';
import  {Component} from 'reflux';
import  {Notify, Button} from 'zent';
import TestStore from 'stores/TestStore';
import TestAction from 'actions/TestAction';

class World extends Component
    constructor:  (props) ->
        super props
        @stores = [TestStore]


    handleOK : ->
        console.log "hello"
        console.log "count state:",

    render: ->
        `(
            <div>
                <h1 onClick={this.handleOK}>Counter Example!</h1>
                <div>
                    <h2> current counter: {this.state.counter}</h2>
                </div>
                <Operate />
            </div>
        )`

class Operate extends Component
    render: ->
      `(
          <div>
              <Button onClick={() => TestAction.increment()}>increment</Button>
              <Button onClick={() => TestAction.decrement(2)}>decrement 2</Button>
          </div>
      )`

export default World