import { Command } from "commander";
import chalk from "chalk";

// Create a new command instance
const program = new Command();

// Set basic information
program
  .name("lere")
  .description("CLI interface for extracting legal roms from various platforms")
  .version("1.0.0");

// Define commands
program
  .command("extract")
  .description("Extract roms from supported platforms")
  .action(() => {
    console.log(chalk.green("Extracting roms..."));
    // This would eventually call functionality from @lere/core
  });

// Add more commands as needed

// Parse command line arguments
program.parse(process.argv);

// If no arguments provided, show help
if (!process.argv.slice(2).length) {
  program.outputHelp();
}
