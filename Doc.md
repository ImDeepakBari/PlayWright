<h3>How to install pytest playwright in pycharm.</h3>
<ul><h4>pip install pytest-playwright</h4>
<li>This will install pytest framework.</li>
<li>Pytest fixture can be directly used with playwright test case</li>

</ul><br>

<ul><h4>playwright install</h4>
<li>This will install browser dependencies for firefox, choromium browser (chroem, edge) and webkit for safari and firefox.</li>

</ul>

# Getting locator/elements in playwright
<h4>Multiple way to locate elements in playwright as below:
</h4>
<ul>(i) page.get_by_role(): Locate elements in dom with implicit and explicit accessibility attribute.
</ul>
<ul>(ii) page.get_by_text(): To locate by text content.</ul>
<ul>(iii) page.get_by_label() : To locate a form control associated label's text.</ul>
<ul>(iv) page.get_by_placeholder(): To locate an input by placeholder.</ul>
<ul>(v) page.get_by_alt_text() to locate an element, usually image, by its text alternative.</ul>
<ul>(vi) page.get_by_title() to locate an element by its title attribute.</ul>
<ul>(vii) page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).</ul>

