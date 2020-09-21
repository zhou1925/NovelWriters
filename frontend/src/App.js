import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import NovelList from './components/NovelList';
import Novel from './components/Novel';

function App() {
  
  return (
    <div>
      <div className="content">
        <Navbar />
        <Switch>
          <Route path="/novels/:id" component={Novel} />
          <Route path="/novels" component={NovelList} />
        </Switch>
      </div>
    </div>
  );
}

export default App;
