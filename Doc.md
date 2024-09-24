<h3>How to install pytest playwright in pycharm.</h3>
<ul><h4>pip install pytest-playwright</h4>
<li>This will install pytest framework.</li>
<li>Pytest fixture can be directly used with playwright test case</li>

</ul><br>

<ul><h4>playwright install</h4>
<li>This will install browser websocket.</li>

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

# Locator:
<h4>Locators are the central piece of Playwright's auto-waiting and retry-ability.</h4>
<ul>Methods for locator are :<br>
<li>(i) all() : <i>returns whatever is present in the page</i></li>
<li>(ii) all_inner_texts</li>
<li>(iii) all_text_contents</li>

<ul><li>eg: button = page.get_by_role("button").and_(page.getByTitle("Subscribe"))</li></ul>

<li>(v) blur()</li>
<li>(vi) bounding_box()</li>
<li>(vii) clear()</li>
<li>(viii) click()</li>
<li>(ix) count(): <i>Returns the number of elements matching the locator.</i></li>
<li>(x) dblclick()</li>
<li>(xi) wait_for(): <i>Returns when element specified by locator satisfies the state option.</i>
<ul><li>state are as : "attached" | "detached" | "visible" | "hidden"</li></ul>
</li>
<li>(xii) drag_to</li>
<li>(xiii) evaluate</li>
<li>(xiv) count</li>
<li>(xv) fill</li>
<li>(xvi) filter</li>
<li>(xvii) focus</li>
<li>(xviii) frame_locator</li>
<li>(xix) get_attribute</li>
<li>(xx) get_by_alt_text</li>
<li>(xxi) get_by_label</li>
<li>(xxii) hover</li>
<li>(xxiii) highlight()</li>
<li>(xxiv) nth</li>
<li>(xxv) or_</li>
<li>(xxvi) press</li>
</ul>

# Locator operators
<ul>

<li> and_ : <i>Creates a locator that matches both this locator and the argument locator.</i>
<li>filter(): This helps to narrow down locator by simply filtering by role, name, text.</li>
<li>or_ : This is used to match one or two alternative locator</li>
<li>visiblle =True: page.locator("button").locator("visible=true").click()</li>
</ul>


# Properties
Some of the properties for locator in playwright are as below:
<ul>
<li>content_frame</li>
<li>first</li>
<li>last</li>
<li>page</li>
</ul>

#Lists
<ul><h5>Count items in a list</h5>
<ul>
<li>expect(page.get_by_role("listitem")).to_have_count(3)</li>
<h5>Assert all text in a list</h5>
<li>expect(page.get_by_role("listitem")).to_have_text(["apple", "banana", "orange"])</li>
<h5>Get a specific item</h5>
<li>Get by text</li>
<li>Filter by text</li>
<li>Get by test id</li>
<li>Get by nth item</li>
</ul></ul>

# Chaining filters
<h5>When you have elements with various similarities, you can use the locator.filter() method to select the right one. You can also chain multiple filters to narrow down the selection.</h5>
<p>eg: row_locator = page.get_by_role("listitem")<br>

row_locator.filter(has_text="Mary").filter(
    has=page.get_by_role("button", name="Say goodbye")<br>
).screenshot(path="screenshot.png")</p>

#