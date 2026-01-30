from playwright.sync_api import sync_playwright


def _collect_non_empty_texts(locator):
    texts = []
    for i in range(locator.count()):
        text = (locator.nth(i).text_content() or "").strip()
        if text:
            texts.append(text)
    return texts


def _wait_for_non_empty_text(page, selector, timeout_ms=2000):
    try:
        page.wait_for_function(
            """
            selector => {
                const el = document.querySelector(selector);
                return el && el.textContent && el.textContent.trim().length > 0;
            }
            """,
            arg=selector,
            timeout=timeout_ms,
        )
    except Exception:
        return []
    return _collect_non_empty_texts(page.locator(selector))


def run_checks():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 2000})

        # Login checks
        page.goto("https://demoqa.com/login", wait_until="domcontentloaded")
        page.wait_for_selector("#userName")
        page.wait_for_selector("#password")

        page.locator("#login").click()
        login_empty_errors = _wait_for_non_empty_text(page, "#name", timeout_ms=1500)
        print("Login empty fields error:", login_empty_errors or None)

        page.fill("#userName", "invalid_user")
        page.fill("#password", "invalid_pass")
        page.locator("#login").click()
        login_invalid_errors = _wait_for_non_empty_text(page, "#name", timeout_ms=3000)
        print("Login invalid credentials error:", login_invalid_errors or None)

        # Register checks
        page.locator("#newUser").scroll_into_view_if_needed()
        page.locator("#newUser").click()
        try:
            page.wait_for_url("**/register", timeout=5000)
        except Exception:
            # Fallback in case the click is intercepted or blocked.
            page.goto("https://demoqa.com/register", wait_until="domcontentloaded")
        page.wait_for_selector("#firstname")
        page.wait_for_selector("#lastname")
        page.wait_for_selector("#userName")
        page.wait_for_selector("#password")

        page.locator("#register").click()
        register_empty_name_errors = _wait_for_non_empty_text(page, "#name", timeout_ms=1500)
        register_empty_output_errors = _wait_for_non_empty_text(page, "#output", timeout_ms=1500)
        print(
            "Register blank fields errors:",
            {
                "name": register_empty_name_errors or None,
                "output": register_empty_output_errors or None,
            },
        )

        page.fill("#firstname", "Test")
        page.fill("#lastname", "User")
        page.fill("#userName", "test_user_demoqa_123")
        page.fill("#password", "Test@1234")
        page.locator("#register").click()
        register_no_captcha_name = _wait_for_non_empty_text(page, "#name", timeout_ms=3000)
        register_no_captcha_output = _wait_for_non_empty_text(page, "#output", timeout_ms=3000)
        print(
            "Register without captcha errors:",
            {
                "name": register_no_captcha_name or None,
                "output": register_no_captcha_output or None,
            },
        )

        browser.close()


if __name__ == "__main__":
    run_checks()
