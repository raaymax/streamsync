import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
	testDir: "./tests",
	fullyParallel: false,
	forbidOnly: !!process.env.CI,
	retries: 2,
	workers: 1,
	reporter: "list",
	use: {
		baseURL: "http://127.0.0.1:7357",
		trace: "on-first-retry",
	},

	projects: [
		{
			name: "chromium",
			use: { ...devices["Desktop Chrome"] },
		},

		{
			name: "firefox",
			use: { ...devices["Desktop Firefox"] },
		},

		{
			name: "webkit",
			use: { ...devices["Desktop Safari"] },
		},
	],

	webServer: {
		command: "npm start",
		url: "http://127.0.0.1:7357",
		reuseExistingServer: true,
		stdout: 'pipe',
	},
});
