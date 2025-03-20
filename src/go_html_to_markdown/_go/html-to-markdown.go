package main

import (
	"C"
	"log"
)
import (
	"github.com/JohannesKaufmann/html-to-markdown/v2/converter"
	"github.com/JohannesKaufmann/html-to-markdown/v2/plugin/base"
	"github.com/JohannesKaufmann/html-to-markdown/v2/plugin/commonmark"
	"github.com/JohannesKaufmann/html-to-markdown/v2/plugin/table"
)

//export ConvertHTMLToMarkdown
func ConvertHTMLToMarkdown(html *C.char) *C.char {
	conv := converter.NewConverter(
		converter.WithPlugins(
			base.NewBasePlugin(),
			commonmark.NewCommonmarkPlugin(
				commonmark.WithStrongDelimiter("__"),
			),

			table.NewTablePlugin(table.WithSkipEmptyRows(true)),
		),
	)

	markdown, err := conv.ConvertString(C.GoString(html))
	if err != nil {
		log.Fatal(err)
	}
	return C.CString(markdown)
}

func main() {
}
