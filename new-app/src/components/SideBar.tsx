import React from "react";
import { Link } from "react-router-dom";

const Sidebar: React.FC = () => {
  return (
    <aside className="w-64 bg-gray-200 h-full shadow-lg">
      <nav className="p-4">
        <ul className="space-y-4">
          <li>
            <Link
              to="/"
              className="block p-2 text-gray-800 hover:bg-gray-300 rounded"
            >
              Dashboard
            </Link>
          </li>
          <li>
            <Link
              to="/faculties"
              className="block p-2 text-gray-800 hover:bg-gray-300 rounded"
            >
              Faculty Management
            </Link>
          </li>
          <li>
            <Link
              to="/students"
              className="block p-2 text-gray-800 hover:bg-gray-300 rounded"
            >
              Student Management
            </Link>
          </li>
          <li>
            <Link
              to="/courses"
              className="block p-2 text-gray-800 hover:bg-gray-300 rounded"
            >
              Course Management
            </Link>
          </li>
          <li>
            <Link
              to="/enquiries"
              className="block p-2 text-gray-800 hover:bg-gray-300 rounded"
            >
              Enquiry Management
            </Link>
          </li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
