import React from 'react';
import './FaixaCTA.css';

import { Router, Link } from "@reach/router"

function FaixaCTA() {
  return (
    <section class="faixa-cta">
        <h4>Compartilhe seus conhecimentos, conheça novas pessoas e ainda ganhe um dinheiro extra.</h4>
        <Link to="/criar-conta" class="btn btn-secondary">TORNE-SE UM INTRUTOR</Link>
    </section>
  );
}

export default FaixaCTA;