import React, {PropTypes} from 'react'
import {
    HashRouter as Router,
    Route,
    Link
} from 'react-router-dom'
import Hello from 'components/Hello'
import Counter from 'components/Counter'


Routes = ->
  `(
  <Router>
        <div>
            <Route exact path="/" component={Hello}/>
            <Route path="/world" component={Counter}/>
        </div>
    </Router>
  )`

export default Routes
