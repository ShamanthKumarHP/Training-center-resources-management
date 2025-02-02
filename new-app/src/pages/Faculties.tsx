import React, { useState } from "react";

type Faculty = {
  id: number;
  name: string;
  email: string;
  expertise: string;
};

const Faculties: React.FC = () => {
  const [facultyList, setFacultyList] = useState<Faculty[]>([
    { id: 1, name: "John Doe", email: "john@example.com", expertise: "Python" },
    { id: 2, name: "Jane Smith", email: "jane@example.com", expertise: "C" },
  ]);

  const handleDelete = (id: number) => {
    setFacultyList((prev) => prev.filter((faculty) => faculty.id !== id));
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Faculty Management</h1>
      <div className="mb-4">
        <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Add New Faculty
        </button>
      </div>
      <table className="min-w-full bg-white border border-gray-300">
        <thead>
          <tr className="bg-gray-200">
            <th className="border px-4 py-2">Name</th>
            <th className="border px-4 py-2">Email</th>
            <th className="border px-4 py-2">Expertise</th>
            <th className="border px-4 py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          {facultyList.map((faculty) => (
            <tr key={faculty.id}>
              <td className="border px-4 py-2">{faculty.name}</td>
              <td className="border px-4 py-2">{faculty.email}</td>
              <td className="border px-4 py-2">{faculty.expertise}</td>
              <td className="border px-4 py-2 text-center">
                <button
                  className="bg-yellow-500 text-white px-2 py-1 rounded hover:bg-yellow-600 mr-2"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(faculty.id)}
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

export default Faculties;