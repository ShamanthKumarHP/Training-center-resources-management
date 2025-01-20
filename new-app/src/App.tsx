import React from "react";
import Navbar from "./components/NavBar";
import Sidebar from "./components/SideBar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex h-screen">
        <Sidebar />
        <div className="flex-1 flex flex-col">
          <Navbar />
          <main className="p-4">
            {/* Routes will be added here */}
          </main>
        </div>
      </div>
    </Router>
  );
};

export default App;
