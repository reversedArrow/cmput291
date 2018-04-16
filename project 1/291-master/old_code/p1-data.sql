-- test data set 1
-- (staff_id, role, name, login, password)
INSERT INTO staff VALUES
('12345', 'A', 'Admin00', 'admin00', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12346', 'A', 'Admin01', 'admin01', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12347', 'A', 'Admin02', 'admin02', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12348', 'D', 'Doctor00', 'doctor00', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12349', 'D', 'Doctor01', 'doctor01', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12350', 'D', 'Doctor02', 'doctor02', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12351', 'N', 'Nurse00', 'nurse00', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12352', 'N', 'Nurse01', 'nurse01', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'),
('12353', 'N', 'Nurse02', 'nurse02', 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057');

-- (hcno, name, age_group, address, phone, emg_phone)
INSERT INTO patients VALUES
('12345', 'Patient01', '18-23', '116 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5050', '780-423-4567'),
('12351', 'Patient01', '24-30', '116 St & 100 Ave, Edmonton, AB T6G 2R3', '780-492-5000', '780-423-2222'),
('12346', 'Patient02', '18-23', '117 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5051', '780-423-4568'),
('12347', 'Patient03', '24-30', '118 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5052', '780-423-4569'),
('12348', 'Patient04', '24-30', '119 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5053', '780-423-4570'),
('12349', 'Patient05', '31-36', '120 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5054', '780-423-4571'),
('12350', 'Patient06', '24-30', '121 St & 85 Ave, Edmonton, AB T6G 2R3', '780-492-5055', '780-423-4572');

-- (chart_id, hcno, adate, edate)
INSERT INTO charts VALUES
('22345', '12345', '2016-10-14', '2016-10-20'),
('22346', '12346', '2016-10-14', NULL),
('22347', '12347', '2016-11-14', '2016-10-15'),
('22348', '12348', '2016-11-14', '2016-10-15'),
('22349', '12349', '2016-10-15', '2016-10-16'),
('22350', '12345', '2016-09-14', '2016-10-12'),
('22351', '12345', '2016-10-25', NULL);

-- (hcno, chart_id, staff_id, osb_date, symptom)
INSERT INTO symptoms VALUES
('12345', '22345', '12348', '2016-10-14', 'Not breathing'),
('12345', '22345', '12348', '2016-10-18', 'Broken arm');

-- (hcno, chart_id, staff_id, ddate, diagnosis)
INSERT INTO diagnoses VALUES
('12345', '22345', '12348', '2016-10-14', 'Ebola'),
('12345', '22346', '12349', '2016-10-12', 'T-Virus'),
('12345', '22345', '12348', '2016-10-15', 'The Abyss');

-- (drug_name, category)
INSERT INTO drugs VALUES
('Abarelix', 'category01'),
('Abatacep', 'category01'),
('Pacerone', 'category02'),
('Pancrelipase', 'category02');

-- (hcno, chart_id, staff_id, mdate, start_med, end_med, amount, drug_name)
INSERT INTO medications VALUES
('12345', '22345', '12348', '2016-10-14', '2016-10-14', '2016-10-30', 30, 'Abarelix'),
('12345', '22345', '12348', '2016-10-17', '2016-10-17', '2016-11-30', 20, 'Pancrelipase'),
('12345', '22345', '12348', '2016-10-19', '2016-10-19', '2016-11-30', 20, 'Abatacep'),
('12346', '22346', '12349', '2016-10-14', '2016-10-14', '2016-10-30', 30, 'Abatacep'),
('12349', '22349', '12349', '2016-10-14', '2016-10-14', '2016-10-25', 15, 'Abatacep'),
('12348', '22348', '12350', '2016-11-14', '2016-11-14', '2016-11-25', 40, 'Pancrelipase');