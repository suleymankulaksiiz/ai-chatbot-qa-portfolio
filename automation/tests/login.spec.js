import { test, expect } from '@playwright/test';

test('TC_LOGIN_001 - Valid Login', async ({ page }) => {

    // Open application
    await page.goto('/');

    // Enter login credentials
    await page.fill('#email', 'test@test.com');
    await page.fill('#password', '123456');

    // Click login button
    await page.click('button');

    // Verify user redirected to chat page
    await expect(page).toHaveURL(/chat.html/);

});