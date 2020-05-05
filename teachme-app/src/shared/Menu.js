import React from 'react';
import './Menu.css';

import { Link } from "@reach/router"

function Menu() {
    return (
        <React.Fragment>
            <div id="menu-sidebar">
               <section class="logo">
                   <h2 class="text-center">Teach.me</h2>
               </section>

                <nav>
                    <li><Link to="#"><i class="fa-fw fas fa-home"/> Home</Link></li>
                </nav>
                
                <nav>
                    <li><Link to="#"><i class="fa-fw fas fa-user"/>  Painel</Link></li>
                    <ul>
                        <li><Link to="#">Minha Conta</Link></li>
                        <li><Link to="#">Minhas Turmas</Link></li>
                        <li><Link to="#">Minhas Aulas</Link></li>
                    </ul>
                </nav>
                <nav>
                    <li><Link to="#">Painel</Link></li>
                </nav>


            </div>
            <div id="menu-shadow">&nbsp;</div>
        </React.Fragment>
    );
}

export default Menu;