import React from 'react';
import './Home.css';

import Hero from './components/Hero'
import Vantagens from './components/Vantagens'
import FaixaCTA from './components/FaixaCTA'

function Home() {
  return (
    <main id="page-home">
      <Hero/>
      <Vantagens/>
      <FaixaCTA/>
    </main>
  );
}

export default Home;