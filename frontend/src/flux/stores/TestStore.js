import Reflux from 'reflux';
import TestAction from 'actions/TestAction';

class TestStore extends Reflux.Store {
    constructor(){
        super();
        this.listenToMany(TestAction);
        this.state = {
            counter: 0
        }
    }

    increment(){
        let count = this.state.counter + 1;
        this.setState({counter: count});
    }

    decrement(step){
        let count = this.state.counter - step;
        this.setState({counter: count});
    }
}

export default TestStore;