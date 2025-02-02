import React, { useState } from "react";

type Enquiry = {
  id: number;
  name: string;
  contactNumber: string;
  courses: string;
  batchPreference: string; // "Morning" or "Evening"
  email: string;
  otherDetails: string;
  newCourse: string;
};

const Enquiries: React.FC = () => {
  const [enquiryList, setEnquiryList] = useState<Enquiry[]>([
    {
      id: 1,
      name: "John Doe",
      contactNumber: "1234567890",
      courses: "Web Development",
      batchPreference: "Morning",
      email: "john@example.com",
      otherDetails: "Interested in project-based learning.",
      newCourse: "N/A",
    },
    {
      id: 2,
      name: "Jane Smith",
      contactNumber: "9876543210",
      courses: "Data Science",
      batchPreference: "Evening",
      email: "jane@example.com",
      otherDetails: "Wants flexible schedules.",
      newCourse: "Advanced Python",
    },
  ]);

  const handleDelete = (id: number) => {
    setEnquiryList((prev) => prev.filter((enquiry) => enquiry.id !== id));
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Enquiry Management</h1>
      <div className="mb-4">
        <button className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Add New Enquiry
        </button>
      </div>
      <table className="min-w-full bg-white border border-gray-300">
        <thead>
          <tr className="bg-gray-200">
            <th className="border px-4 py-2">Name</th>
            <th className="border px-4 py-2">Contact Number</th>
            <th className="border px-4 py-2">Courses</th>
            <th className="border px-4 py-2">Batch Preference</th>
            <th className="border px-4 py-2">Email</th>
            <th className="border px-4 py-2">Other Details</th>
            <th className="border px-4 py-2">New Course</th>
            <th className="border px-4 py-2">Actions</th>
          </tr>
        </thead>
        <tbody>
          {enquiryList.map((enquiry) => (
            <tr key={enquiry.id}>
              <td className="border px-4 py-2">{enquiry.name}</td>
              <td className="border px-4 py-2">{enquiry.contactNumber}</td>
              <td className="border px-4 py-2">{enquiry.courses}</td>
              <td className="border px-4 py-2">{enquiry.batchPreference}</td>
              <td className="border px-4 py-2">{enquiry.email}</td>
              <td className="border px-4 py-2">{enquiry.otherDetails}</td>
              <td className="border px-4 py-2">{enquiry.newCourse}</td>
              <td className="border px-4 py-2 text-center">
                <button
                  className="bg-yellow-500 text-white px-2 py-1 rounded hover:bg-yellow-600 mr-2"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(enquiry.id)}
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

export default Enquiries;
