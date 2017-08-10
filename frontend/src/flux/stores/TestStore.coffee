import Reflux from 'reflux';
import TestAction from 'actions/TestAction';

class TestStore extends Reflux.Store

    constructor: (props)->
        super props
        @listenToMany TestAction
        @state =
            counter: 0

    increment: ->
        count = @state.counter + 1
        @setState counter: count

    decrement: (step) ->
        count = @state.counter - step
        @setState counter: count


export default TestStore;