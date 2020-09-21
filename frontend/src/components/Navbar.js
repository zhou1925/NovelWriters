import React from "react";
import { Link } from 'react-router-dom';

const NavBar = () => {
  return (
    <div className="border-b p-4">
      <ul className="flex">
        <li className="mr-6">
          <Link className="text-blue-500 hover:text-blue-800" to="/">Home</Link>
        </li>
        <li>
          <Link className="text-blue-500 hover:text-blue-800" to="/novels">Novels</Link>
        </li>
      </ul>
    </div>
  );
};

export default NavBar;