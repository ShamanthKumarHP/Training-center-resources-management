import React, { useState } from "react";

type Course = {
  id: number;
  name: string;
  startDate: string;
  endDate: string;
  fees: number;
  prerequisites: string;
};

const Courses: React.FC = () => {
  const [courseList, setCourseList] = useState<Course[]>([
    {
      id: 1,
      name: "Web Development",
      startDate: "2025-02-01",
      endDate: "2025-04-30",
      fees: 500,
      prerequisites: "Basic HTML and CSS knowledge",
    },
    {
      id: 2,
      name: "Data Science",
      startDate: "2025-03-01",
      endDate: "2025-06-30",
      fees: 1000,
      prerequisites: "Basic Python knowledge",
    },
  ]);

  const handleDelete = (id: number) => {
    setCourseList((prev) => prev.filter((course) => course.id !== id));
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Course Management</h1>
      <div className="mb-4">
        <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Add New Course
        </button>
      </div>
      <table className="min-w-full bg-white border border-gray-300">
        <thead>
          <tr className="bg-gray-200">
            <th className="border px-4 py-2">Name</th>
            <th className="border px-4 py-2">Start Date</th>
            <th className="border px-4 py-2">End Date</th>
            <th className="border px-4 py-2">Fees</th>
            <th className="border px-4 py-2">Prerequisites</th>
            <th className="border px-4 py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          {courseList.map((course) => (
            <tr key={course.id}>
              <td className="border px-4 py-2">{course.name}</td>
              <td className="border px-4 py-2">{course.startDate}</td>
              <td className="border px-4 py-2">{course.endDate}</td>
              <td className="border px-4 py-2">{`$${course.fees}`}</td>
              <td className="border px-4 py-2">{course.prerequisites}</td>
              <td className="border px-4 py-2 text-center">
                <button
                  className="bg-yellow-500 text-white px-2 py-1 rounded hover:bg-yellow-600 mr-2"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(course.id)}
                  className="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Courses;
