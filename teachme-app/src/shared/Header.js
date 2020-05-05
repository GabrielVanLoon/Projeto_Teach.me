import React from 'react';
import './Header.css';

import { Router, Link } from "@reach/router"

function Header() {
  return (
    <header id="header">
      <div class="logo">
        <button id="btn-menu"><i class="fa-fw fas fa-bars"/></button>
        <h2><Link to="/">Teach.me</Link></h2>
      </div>
      <div class="sign-in">
          <Link to="login" className="btn">Entrar</Link>
          <small>Ainda não possui conta? <a href="#">Clique aqui.</a></small>
      </div>
    </header>
  );
}

export default Header;
