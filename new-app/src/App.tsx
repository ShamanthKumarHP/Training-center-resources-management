import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";

import Faculties from "./pages/Faculties";
import Students from "./pages/Students";
import Courses from "./pages/Courses";
import Enquiries from "./pages/Enquiries";
import Dashboard from "./pages/Dashboard";

const App: React.FC = () => {
  return (
    <Router>
      <div className="flex h-screen">
        <Sidebar />
        <div className="flex-1 flex flex-col">
          <Navbar />
          <main className="p-4">
            <Routes>
              <Route path="/faculties" element={<Faculties />} />
              <Route path="/students" element={<Students />} />
              <Route path="/courses" element={<Courses />} />
              <Route path="/enquiries" element={<Enquiries />} />
              <Route path="/" element={<Dashboard />} />
              {/* Other routes */}
            </Routes>
          </main>
        </div>
      </div>
    </Router>
  );
};

export default App;
