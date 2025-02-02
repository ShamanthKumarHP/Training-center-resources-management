import React from "react";

const Dashboard: React.FC = () => {
  // Example static data (Replace with dynamic data fetched from your backend)
  const totalFaculties = 20;
  const totalCourses = 15;
  const totalStudents = 200;
  const mostEnquiredCourse = "Web Development";

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

      {/* Cards Section */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        {/* Total Faculties */}
        <div className="bg-blue-500 text-white p-6 rounded shadow">
          <h2 className="text-lg font-bold">Total Faculties</h2>
          <p className="text-3xl mt-2">{totalFaculties}</p>
        </div>

        {/* Total Courses */}
        <div className="bg-green-500 text-white p-6 rounded shadow">
          <h2 className="text-lg font-bold">Total Courses</h2>
          <p className="text-3xl mt-2">{totalCourses}</p>
        </div>

        {/* Total Students */}
        <div className="bg-purple-500 text-white p-6 rounded shadow">
          <h2 className="text-lg font-bold">Total Students</h2>
          <p className="text-3xl mt-2">{totalStudents}</p>
        </div>

        {/* Most Enquired Course */}
        <div className="bg-yellow-500 text-white p-6 rounded shadow">
          <h2 className="text-lg font-bold">Most Enquired Course</h2>
          <p className="text-xl mt-2">{mostEnquiredCourse}</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
