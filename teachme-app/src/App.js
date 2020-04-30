import React from 'react';
import './App.css';

import Header from './shared/Header';
import Footer from './shared/Footer';

import Home from './home/Home'


function App() {
  return (
    <React.Fragment>
      <div id="body-wrapper">
        <Header/>
        <Home/>
        <Footer/>
      </div>
    </React.Fragment>
  );
}

export default App;
