import fs from 'fs';
import path from 'path';

export async function GET() {
	const staticFolder = path.resolve('static'); // Ensure the path is correctly resolved
	try {
		// Read the contents of the static folder
		const files = fs.readdirSync(staticFolder);
		return new Response(JSON.stringify(files), {
			headers: { 'Content-Type': 'application/json' }
		});
	} catch (error) {
		return new Response(JSON.stringify({ error: 'Unable to read static folder', details: error.message }), {
			status: 500,
			headers: { 'Content-Type': 'application/json' }
		});
	}
}
