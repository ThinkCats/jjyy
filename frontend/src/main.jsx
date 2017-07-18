import React from 'react';
import ReactDOM from  'react-dom';
import 'antd/dist/antd.less';
import Routes from './routes/index';

main();

function main() {
    ReactDOM.render(<Routes />, document.getElementById('app'));
}
