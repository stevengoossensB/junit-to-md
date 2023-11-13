import xml.etree.ElementTree as ET

def parse_junit_xml(file_path):
    """
    Parses a JUnit XML file and extracts test suite data.

    Args:
        file_path (str): Path to the JUnit XML file.

    Returns:
        list of dict: A list of dictionaries, each representing a test case.
    """
    test_cases = []
    tree = ET.parse(file_path)
    root = tree.getroot()

    for testcase in root.iter('testcase'):
        case = {
            'name': testcase.get('name'),
            'classname': testcase.get('classname'),
            'time': testcase.get('time'),
            'status': 'PASSED'
        }

        failure = testcase.find('failure')
        error = testcase.find('error')
        if failure is not None:
            case['status'] = 'FAILED'
            case['message'] = failure.get('message')
        elif error is not None:
            case['status'] = 'ERROR'
            case['message'] = error.get('message')

        test_cases.append(case)

    return test_cases

def convert_to_markdown(test_cases):
    """
    Converts test case data into Markdown format using a table.

    Args:
        test_cases (list of dict): List of test case data.

    Returns:
        str: A string in Markdown format.
    """
    markdown = "# Test Results\n\n"
    markdown += "| Test Name | Class | Time (s) | Status | Message |\n"
    markdown += "|-----------|-------|---------|--------|---------|\n"

    for case in test_cases:
        message = case.get('message', '')
        markdown += f"| {case['name']} | {case['classname']} | {case['time']} | {case['status']} | {message} |\n"

    return markdown

def convert_file(input_file, output_file):
    """
    Converts a JUnit XML file to a Markdown file.

    Args:
        input_file (str): Path to the JUnit XML file.
        output_file (str): Path to the output Markdown file.
    """
    test_cases = parse_junit_xml(input_file)
    markdown = convert_to_markdown(test_cases)
    with open(output_file, 'w') as md_file:
        md_file.write(markdown)
